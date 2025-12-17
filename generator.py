import csv
import os
from datetime import datetime

# 設定檔案路徑
CSV_FILE = 'products.csv'
OUTPUT_DIR = '_posts'

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def generate_post(row):
    # 自動清除欄位名稱前後的空格，防止 KeyError
    row = {k.strip().lower(): v for k, v in row.items()}
    
    # 取得欄位內容 (加上預設值防止當機)
    title = row.get('title', '未命名文章')
    tags_raw = row.get('tags', '')
    price = row.get('price', 'N/A')
    summary = row.get('summary', '無摘要')
    affiliate_link = row.get('affiliate_link', '#')
    
    # 處理標籤
    tags_list = [t.strip() for t in tags_raw.split(',')] if tags_raw else []
    tags_str = '[' + ', '.join(f'"{t}"' for t in tags_list) + ']'
    
    # 判斷導購區塊
    if "頭皮護理" in tags_list:
        cta_block = f"""
<div class="cta-box">
  <p style="color: #e64a19; font-weight: bold;">這項產品是我們嚴選的頭皮護理基石。立即行動！</p>
  <a href="{affiliate_link}" class="buy-button" target="_blank">查看專業選品組優惠</a>
</div>"""
    else:
        cta_block = f"""
<div class="cta-box">
  <a href="{affiliate_link}" class="buy-button" target="_blank">前往領取今日限定優惠</a>
</div>"""

    return f"""---
layout: post
title: {title}
date: {datetime.now().strftime('%Y-%m-%d')}
tags: {tags_str}
price: {price}
summary: {summary}
---

## 🌟 選品智庫實測推薦：{title}

經過我們團隊針對各平台的優惠力度與產品品質進行評測，這項選品在今日具備極高的入手機會。

### 💎 為什麼推薦這個連結？
* **官方授權**：確保來源正當，售後有保障。
* **價格優勢**：連結已自動帶入當前最新促銷代碼。

{cta_block}
"""

# 執行生成
try:
    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        
        # 檢查 CSV 的標題列到底長怎樣
        headers = [h.strip().lower() for h in reader.fieldnames]
        if 'filename' not in headers:
            print(f"❌ 錯誤：CSV 檔案中找不到 'filename' 欄位！")
            print(f"目前偵測到的欄位有：{reader.fieldnames}")
            exit()

        for row in reader:
            # 取得檔名並自動清除空格
            raw_filename = row.get('filename') or row.get('FileName') or "post.md"
            filename = f"{datetime.now().strftime('%Y-%m-%d')}-{raw_filename.strip()}"
            
            with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as out_f:
                out_f.write(generate_post(row))
            print(f"✅ 檔案已生成：{filename}")

except Exception as e:
    print(f"❌ 執行出錯：{e}")