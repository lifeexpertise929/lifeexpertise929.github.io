import csv
import os
from datetime import datetime

# 確保輸出目錄存在
if not os.path.exists('_posts'):
    os.makedirs('_posts')

today = datetime.now().strftime('%Y-%m-%d')

try:
    with open('products.csv', mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        reader.fieldnames = [name.strip() for name in reader.fieldnames]
        
        count = 0
        for row in reader:
            row = {k.strip(): v.strip() for k, v in row.items() if k}
            fname = row.get('filename')
            if not fname: continue
            
            # 分類邏輯：取標籤的第一個詞
            raw_tags = row.get('tags', '其他')
            tag_list = [t.strip() for t in raw_tags.split(',')]
            main_category = tag_list[0] if tag_list else "其他"
            
            title = row.get('title', '限時優惠')
            filename = f"{today}-{fname.replace('.md', '')}.md"
            filepath = os.path.join('_posts', filename)
            
            content = f"""---
layout: post
title: "{title}"
price: "{row.get('price', '立即查看')}"
summary: "{row.get('summary', '')}"
rating: "{row.get('rating', '4.8')}"
data_source: "{row.get('data_source', '官方認證')}"
category: "{main_category}"
tags: {tag_list}
---
### {title} 2025 最新優惠
{row.get('summary', '')}

**[👉 點此立即領取優惠]({row.get('affiliate_link', '#')})**
"""
            with open(filepath, 'w', encoding='utf-8') as wf:
                wf.write(content)
            count += 1
            
        print(f"✨ 網頁檔案產生完成！共處理 {count} 篇。")
except Exception as e:
    print(f"❌ 錯誤：{e}")