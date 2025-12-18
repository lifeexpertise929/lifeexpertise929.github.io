import csv
import os
from datetime import datetime

# 1. 確保 _posts 資料夾存在
if not os.path.exists('_posts'):
    os.makedirs('_posts')
else:
    # 執行前先清空舊檔案，確保資料最新
    for file in os.listdir('_posts'):
        if file.endswith('.md'):
            os.remove(os.path.join('_posts', file))

today = datetime.now().strftime('%Y-%m-%d')

# 2. 使用 utf-8-sig 來自動處理 Excel 的隱形 BOM 字元
try:
    with open('products.csv', mode='r', encoding='utf-8-sig') as f:
        # 使用 DictReader 讀取，並自動修復標題欄位的空白
        reader = csv.DictReader(f)
        reader.fieldnames = [name.strip() for name in reader.fieldnames]
        
        count = 0
        for row in reader:
            # 取得欄位資料，並處理前後空格
            fname = row.get('filename', '').strip()
            title = row.get('title', '').strip()
            
            # 如果抓不到 filename，跳過該行以防報錯
            if not fname:
                continue
                
            filename = f"{today}-{fname}.md"
            filepath = os.path.join('_posts', filename)
            
            # 寫入 Markdown 內容，包含您要的星等 (rating)
            content = f"""---
layout: post
title: "{title}"
price: "{row.get('price', '').strip()}"
summary: "{row.get('summary', '').strip()}"
rating: "{row.get('rating', '4.5').strip()}"
tags: [{row.get('tags', '').strip()}]
---
這是 {title} 的詳細優惠資訊。
"""
            with open(filepath, 'w', encoding='utf-8') as wf:
                wf.write(content)
            count += 1
            
        print(f"✅ 成功！已從 CSV 產生 {count} 篇商品檔案。")

except FileNotFoundError:
    print("❌ 錯誤：找不到 products.csv，請確認檔案在同一個資料夾。")
except Exception as e:
    print(f"❌ 發生錯誤：{e}")