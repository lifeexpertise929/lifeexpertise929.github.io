import csv
import os
from datetime import datetime

# 確保輸出目錄存在
if not os.path.exists('_posts'):
    os.makedirs('_posts')

today = datetime.now().strftime('%Y-%m-%d')

# 使用 utf-8-sig 處理 Excel 可能產生的隱形字元 (BOM)
try:
    with open('products.csv', mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        
        # 檢查 CSV 實際抓到的欄位名稱，幫您除錯
        fieldnames = [field.strip() for field in reader.fieldnames]
        print(f"目前偵測到的欄位有: {fieldnames}")

        count = 0
        for row in reader:
            # 去除欄位內容兩端的空白
            row = {k.strip(): v.strip() for k, v in row.items() if k}
            
            # 取得檔名，若找不到則用編號代替
            fname = row.get('filename') or row.get('檔案名稱') or f"product-{count}"
            title = row.get('title') or row.get('標題', '未命名商品')
            
            filename = f"{today}-{fname}.md"
            filepath = os.path.join('_posts', filename)
            
            content = f"""---
layout: post
title: "{title}"
price: "{row.get('price', '立即查看')}"
summary: "{row.get('summary', '')}"
rating: "{row.get('rating', '4.8')}"
tags: [{row.get('tags', '熱門選品')}]
---
這是 {title} 的詳細內容。
"""
            with open(filepath, 'w', encoding='utf-8') as wf:
                wf.write(content)
            count += 1
            
        print(f"✨ 成功產生 {count} 篇商品文案！請檢查 _posts 資料夾。")

except FileNotFoundError:
    print("❌ 錯誤：找不到 products.csv 檔案。")
except Exception as e:
    print(f"❌ 發生預期外的錯誤: {e}")