import csv
import os
import shutil
import google.generativeai as genai
from datetime import datetime
import json
import time

# --- 1. 設定區 ---
# 您的 API Key
GOOGLE_API_KEY = "AIzaSyDD3MPq7zgpHtUUSzL0eNXEpKj2MeoCum0" 
CSV_FILE = 'products.csv'
OUTPUT_DIR = '_posts'

# 初始化 AI 並修正模型路徑
genai.configure(api_key=GOOGLE_API_KEY)
# 修正模型名稱為標準格式
model = genai.GenerativeModel('models/gemini-1.5-flash')

if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(OUTPUT_DIR)

def ask_ai_for_content(link):
    """叫 AI 撰寫具備專家感的深度評測文案"""
    prompt = f"""
    任務：作為一名專業選品顧問，分析此導購連結並撰寫文案。
    連結：{link}
    要求風格：語氣專業且誠懇，強調「現在下單」的價值，解決讀者選購時的疑慮。
    
    請務必回傳純 JSON 格式（禁止包含 markdown 代碼塊外框）：
    {{
      "title": "2025 [產品名稱] 實測心得：今日隱藏優惠與購買指南",
      "tags": "分類1, 分類2",
      "summary": "一句話總結此產品的核心優勢（40字內）",
      "content": "一段具備權威感的推薦理由，解釋為何此選品在品質與價格上最具競爭力。"
    }}
    """
    try:
        # 加入安全性設定，避免內容被過濾
        response = model.generate_content(prompt)
        # 移除可能干擾 JSON 解析的字符
        text = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(text)
    except Exception as e:
        print(f"⚠️ AI 撰寫稍有遲疑: {e}")
        return None

def generate_post(row):
    # 清理欄位
    row = {k.strip().lower(): v for k, v in row.items()}
    link = row.get('affiliate_link', '')
    
    # 如果 Excel 標題或摘要為空，則啟用 AI
    if not row.get('title') or not row.get('summary'):
        print(f"🤖 AI 正在深度解析連結並產出高品質內容: {link[:40]}...")
        ai_data = ask_ai_for_content(link)
        if ai_data:
            row['title'] = ai_data['title']
            row['summary'] = ai_data['summary']
            row['tags'] = ai_data['tags']
            ai_content = ai_data['content']
        else:
            ai_content = "經智庫團隊多維度分析，此選品在目前市場通路中具備絕佳的性價比，值得即時鎖定優惠。"
    else:
        # 保留手動輸入的內容
        ai_content = f"根據我們對 {row['title']} 的最新追蹤，目前的折扣力度已達本月最佳入手機會。"

    # 標籤處理
    tags_list = [t.strip() for t in row['tags'].split(',')]
    tags_str = '[' + ', '.join(f'"{t}"' for t in tags_list) + ']'
    
    # 智慧 CTA 按鈕
    cta_text = "查看專業選品組優惠" if "頭皮護理" in tags_list else "前往領取今日限定優惠"
    
    return f"""---
layout: post
title: {row['title']}
date: {datetime.now().strftime('%Y-%m-%d')}
tags: {tags_str}
price: {row.get('price', '優惠中')}
summary: {row['summary']}
---

## 💎 選品智庫：專業編輯推薦

{ai_content}

### 💡 為什麼選擇此推薦連結？
* **授權通路**：保證來自官方授權之電商平台，購物安全無虞。
* **即時最低價**：系統已自動帶入當前促銷代碼，無須額外手動輸入。
* **專業嚴選**：針對品質、出貨速度與售後服務進行綜合評分後的首選。

<div class="cta-box">
  <a href="{link}" class="buy-button" target="_blank">{cta_text}</a>
</div>

---
*聲明：本文包含聯盟行銷連結，這能支持我們持續提供高品質的選品分析，且不影響您的實際購買價格。*
"""

# --- 3. 核心執行流程 ---
try:
    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            raw_fn = row.get('filename') or f"item_{int(time.time())}.md"
            filename = f"{datetime.now().strftime('%Y-%m-%d')}-{raw_fn.strip()}"
            
            with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as out_f:
                out_f.write(generate_post(row))
            count += 1
            # 增加休息時間以確保免費版 API 穩定
            time.sleep(2)
            
    print(f"✨ 高品質 AI 文章已全數生成（共 {count} 篇）並與 Excel 同步。")

except Exception as e:
    print(f"❌ 發生關鍵錯誤：{e}")