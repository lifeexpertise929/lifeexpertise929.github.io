import csv
import os
import shutil
from datetime import datetime
import time

# --- 1. 設定與清理 ---
CSV_FILE = 'products.csv'
OUTPUT_DIR = '_posts'

# 強制清空舊檔，確保網站不留垃圾文章
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(OUTPUT_DIR)

def generate_post(row):
    # 清理欄位空格並標準化
    row = {k.strip().lower(): v.strip() for k, v in row.items()}
    
    title = row.get('title', '精選優惠文章')
    summary = row.get('summary', '查看最新優惠資訊。')
    tags_raw = row.get('tags', '選品智庫')
    price = row.get('price', '限時優惠中')
    link = row.get('affiliate_link', '#')
    
    # 格式化標籤
    tags_list = [t.strip() for t in tags_raw.split(',')]
    tags_str = '[' + ', '.join(f'"{t}"' for t in tags_list) + ']'
    
    # 智慧型按鈕文字邏輯
    cta_text = "查看專業選品組優惠" if "頭皮護理" in tags_list else "立即前往領取折扣"

    # 專業排版模板
    content = f"""---
layout: post
title: "{row.get('title')}"
price: "{row.get('price')}"
summary: "{row.get('summary')}"
rating: "{rating}"
---

### 💎 智庫推薦理由
這項選品經過我們團隊的綜合評估，無論在**價格競爭力**還是**通路安全性**上都表現優異。

> **編輯筆記：**
> {summary}

### 💡 為什麼選擇此路徑？
* **即時價格保障**：此連結已鎖定今日最優價格，無須額外搜尋折扣碼。
* **官方直送授權**：確保貨源來自品牌官方或大型電商，售後無慮。
* **限量配額**：熱門優惠隨時可能結束，建議優先點擊確認。

<div class="cta-box">
  <p style="font-weight: bold; color: #d32f2f;">🔥 當前狀態：{price}</p>
  <a href="{link}" class="buy-button" target="_blank">{cta_text}</a>
</div>

---
*讀者聲明：本站專注於推薦高品質購物路徑。透過此連結購買可能為本站帶來微薄支持，但不影響您的購買價格。*
"""
    return content

# --- 2. 執行生成 ---
try:
    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            # 優先使用 Excel 指定的 filename
            raw_fn = row.get('filename') or f"post_{int(time.time())}.md"
            filename = f"{datetime.now().strftime('%Y-%m-%d')}-{raw_fn.strip()}"
            
            with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as out_f:
                out_f.write(generate_post(row))
            count += 1
            
    print(f"✨ 專業版網站更新完成！共導入 {count} 篇 Excel 專屬文案。")

except Exception as e:
    print(f"❌ 發生錯誤：{e}")