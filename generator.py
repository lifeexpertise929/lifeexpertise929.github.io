import csv
import os
from datetime import datetime

# 1. 確保 _posts 資料夾存在，並清空舊檔案以確保資料同步
if not os.path.exists('_posts'):
    os.makedirs('_posts')
else:
    for file in os.listdir('_posts'):
        if file.endswith('.md'):
            os.remove(os.path.join('_posts', file))

# 設定今天的日期（Jekyll 檔案名稱規範）
today = datetime.now().strftime('%Y-%m-%d')

# 2. 讀取 products.csv 並產生 Markdown 檔案
try:
    # 使用 utf-8-sig 處理 Excel 產生的 BOM 字元，避免標題抓不到
    with open('products.csv', mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        # 自動修復欄位名稱前後可能存在的空白
        reader.fieldnames = [name.strip() for name in reader.fieldnames]
        
        count = 0
        for row in reader:
            # 清理資料內容的空白
            row = {k.strip(): v.strip() for k, v in row.items() if k}
            
            # 取得關鍵欄位
            fname = row.get('filename')
            title = row.get('title', '未命名商品')
            
            # 如果 CSV 的檔名有帶 .md，我們把它去掉，由程式統一格式
            if fname and fname.endswith('.md'):
                fname = fname.replace('.md', '')
            
            # 沒檔名就跳過這行
            if not fname:
                continue
                
            # 設定檔案路徑
            filename = f"{today}-{fname}.md"
            filepath = os.path.join('_posts', filename)
            
            # 組合 Markdown 標頭 (Front Matter)
            # 包含：標題、價格、摘要、評分、數據來源、標籤
            content = f"""---
layout: post
title: "{title}"
price: "{row.get('price', '立即查看')}"
summary: "{row.get('summary', '')}"
rating: "{row.get('rating', '4.8')}"
data_source: "{row.get('data_source', '官方認證推薦')}"
tags: [{row.get('tags', '精選優惠')}]
---
這是 {title} 的詳細內容與領券連結。
"""
            # 寫入檔案
            with open(filepath, 'w', encoding='utf-8') as wf:
                wf.write(content)
            count += 1
            
        print(f"✅ 成功！已從 CSV 產生 {count} 篇包含「真實數據來源」的商品檔案。")

except FileNotFoundError:
    print("❌ 錯誤：找不到 products.csv，請確認檔案放在同一個資料夾。")
except Exception as e:
    print(f"❌ 發生錯誤：{e}")