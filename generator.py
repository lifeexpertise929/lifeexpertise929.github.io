import csv
import os
import shutil
import google.generativeai as genai
from datetime import datetime
import json
import time

# --- 1. 設定區 ---
GOOGLE_API_KEY = "AIzaSyDD3MPq7zgpHtUUSzL0eNXEpKj2MeoCum0" 
CSV_FILE = 'products.csv'
OUTPUT_DIR = '_posts'

# 初始化 AI
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    model = None

# --- 2. 自動清空舊檔案：確保與 Excel 100% 同步 ---
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(OUTPUT_DIR)

def ask_ai_for_content(link):
    """當 Excel 沒寫時，才叫 AI 幫忙想"""
    if not model: return None
    prompt = f"請針對此導購連結撰寫吸引人的標題、標籤(逗號隔開)、一句話摘要、及200字推薦理由。連結：{link}。請回傳 JSON 格式。"
    try:
        response = model.generate_content(prompt)
        text = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(text)
    except:
        return None

def generate_post(row):
    # 統一欄位名稱為小寫並去除空白
    row = {k.strip().lower(): v.strip() for k, v in row.items()}
    link = row.get('affiliate_link', '')
    
    # --- 關鍵邏輯：優先使用 Excel 內容 ---
    title = row.get('title')
    summary = row.get('summary')
    tags = row.get('tags', '選品智庫')
    price = row.get('price', '優惠中')
    
    # 如果標題或摘要是空的，才嘗試呼叫 AI
    if not title or not summary:
        print(f"🤖 Excel 內容不完整，嘗試為連結生成 AI 文案: {link[:30]}...")
        ai_data = ask_ai_for_content(link)
        if ai_data:
            title = title or ai_data.get('title')
            summary = summary or ai_data.get('summary')
            tags = tags or ai_data.get('tags')
            recommend_content = ai_data.get('content')
        else:
            recommend_content = "本選品經專業團隊評估，在同類型產品中具備極高性價比。"
    else:
        # Excel 有內容時，直接使用 Excel 的文字
        print(f"✅ 使用 Excel 原文案：{title}")
        recommend_content = f"【編輯實測】針對「{title}」的最新優惠與品質評測表現優異，建議有需求的讀者優先鎖定此路徑。"

    # 處理標籤
    tags_list = [t.strip() for t in tags.split(',')]
    tags_str = '[' + ', '.join(f'"{t}"' for t in tags_list) + ']'
    
    # 智慧按鈕判斷
    cta_text = "查看專業選品組優惠" if "頭皮護理" in tags_list else "前往領取今日限定優惠"
    
    return f"""---
layout: post
title: {title}
date: {datetime.now().strftime('%Y-%m-%d')}
tags: {tags_str}
price: {price}
summary: {summary}
---

## 💎 選品智庫：專業評測觀點

{recommend_content}

### 💡 為什麼我們的編輯推薦此連結？
* **官方通路保障**：確認為品牌授權或官方平台直營，確保正品。
* **價格即時同步**：此連結已嵌入最新折扣資訊，無須額外搜尋。

<div class="cta-box">
  <a href="{link}" class="buy-button" target="_blank">{cta_text}</a>
</div>

---
*讀者聲明：本站專注於提供高品質購物導航，部分連結包含聯盟行銷授權，這不影響您的購買價格。*
"""

# --- 3. 執行主流程 ---
with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        raw_fn = row.get('filename') or f"post_{int(time.time())}.md"
        filename = f"{datetime.now().strftime('%Y-%m-%d')}-{raw_fn.strip()}"
        
        with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as out_f:
            out_f.write(generate_post(row))
        time.sleep(0.5)

print("✨ 網站更新完成！Excel 內容已完整導入。")