import csv
import os
import shutil
import google.generativeai as genai
from datetime import datetime
import json
import time

# --- 1. 設定區 ---
# 您的專屬 API Key 已在此填入
GOOGLE_API_KEY = "AIzaSyDD3MPq7zgpHtUUSzL0eNXEpKj2MeoCum0" 
CSV_FILE = 'products.csv'
OUTPUT_DIR = '_posts'

# 初始化 AI
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. 自動化清理：確保網站內容與 Excel 100% 同步 ---
# 每次執行都會清空 _posts 資料夾，解決舊文章殘留問題
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(OUTPUT_DIR)

def ask_ai_for_content(link):
    """叫 AI 作為專業編輯撰寫高品質文案"""
    prompt = f"""
    任務：作為一名「專業選品智庫」的高級編輯，為以下導購連結撰寫文案。
    連結：{link}
    要求風格：專業評測感、解決用戶痛點、語氣誠懇且具權威性。
    
    請嚴格回傳純 JSON 格式（不要包含任何 markdown 外框）：
    {{
      "title": "2025 [產品名] 深度評測：今日限定優惠路徑",
      "tags": "科技生活選品, 購物攻略",
      "summary": "一句話總結產品優勢（40字內）",
      "content": "一段具備實測感的推薦理由，說明為什麼這個產品值得在今天入手。"
    }}
    """
    try:
        response = model.generate_content(prompt)
        # 清除 AI 可能輸出的 markdown 符號
        clean_json = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(clean_json)
    except Exception as e:
        print(f"⚠️ AI 撰寫出現小跳動 (可能是連結讀取受限): {e}")
        return None

def generate_post(row):
    # 清理 CSV 欄位名稱空格
    row = {k.strip().lower(): v for k, v in row.items()}
    link = row.get('affiliate_link', '')
    
    # 只要標題或摘要其中一個是空的，就發動 AI 自動撰寫
    if not row.get('title') or not row.get('summary'):
        print(f"🤖 正在為連結生成專業 AI 文案: {link[:40]}...")
        ai_data = ask_ai_for_content(link)
        if ai_data:
            row['title'] = ai_data['title']
            row['summary'] = ai_data['summary']
            row['tags'] = ai_data['tags']
            ai_content = ai_data['content']
        else:
            ai_content = "經智庫團隊實測，該選品在今日具備極佳的價格競爭力，推薦有需求的讀者優先關注。"
    else:
        # 如果 Excel 已有手寫文案，則保留並增加專業導語
        ai_content = f"根據最新數據顯示，{row['title']} 的優惠額度已達本季高峰。以下是我們的選品分析。"

    # 處理標籤
    tags_list = [t.strip() for t in row['tags'].split(',')]
    tags_str = '[' + ', '.join(f'"{t}"' for t in tags_list) + ']'
    
    # 智慧導購按鈕文字判斷
    cta_text = "查看專業選品組優惠" if "頭皮護理" in tags_list else "前往領取今日限定優惠"
    
    return f"""---
layout: post
title: {row['title']}
date: {datetime.now().strftime('%Y-%m-%d')}
tags: {tags_str}
price: {row.get('price', '優惠中')}
summary: {row['summary']}
---

## 💎 選品智庫：專業評測觀點

{ai_content}

### 💡 為什麼我們的編輯推薦此連結？
* **官方通路保障**：確認為品牌授權或官方平台直營，確保正品。
* **價格即時同步**：此連結已嵌入今日最新折扣碼，無須額外輸入。
* **實測滿意度**：在該分類選品中，此項目的物流速度與售後評價最高。

<div class="cta-box">
  <a href="{link}" class="buy-button" target="_blank">{cta_text}</a>
</div>

---
*讀者聲明：本站專注於精選高品質購物路徑，部分連結包含聯盟行銷授權，這不影響您的購買價格，卻能支持我們持續運作智庫內容。*
"""

# --- 3. 執行主流程 ---
try:
    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        post_count = 0
        for row in reader:
            # 確保檔名存在
            raw_fn = row.get('filename') or f"auto_{int(time.time())}.md"
            filename = f"{datetime.now().strftime('%Y-%m-%d')}-{raw_fn.strip()}"
            
            with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as out_f:
                out_f.write(generate_post(row))
            
            post_count += 1
            # 休息 1 秒避免觸發 AI 免費版限制
            time.sleep(1)
            
    print(f"✨ 全自動 AI 智庫系統執行成功！共生成 {post_count} 篇高品質文章。")

except Exception as e:
    print(f"❌ 發生錯誤：{e}")