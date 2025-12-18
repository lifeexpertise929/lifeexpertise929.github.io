import csv, os
from datetime import datetime

POSTS_DIR = '_posts'
if not os.path.exists(POSTS_DIR): os.makedirs(POSTS_DIR)
today = datetime.now().strftime('%Y-%m-%d')

def generate_safe_posts():
    try:
        with open('products.csv', mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            reader.fieldnames = [n.strip() for n in reader.fieldnames]
            
            for row in reader:
                row = {k.strip(): v.strip() for k, v in row.items() if k}
                fname = row.get('filename')
                if not fname: continue
                
                # 清理數據防止破版
                title = row.get('title', '限時優惠').replace('"', '\\"')
                summary = row.get('summary', '').replace('"', '\\"').replace('\n', ' ')
                tag_list = [t.strip() for t in row.get('tags', '精選').split(',')]
                
                clean_fname = fname.replace('.md', '')
                filepath = os.path.join(POSTS_DIR, f"{today}-{clean_fname}.md")
                
                content = f"""---
layout: post
title: "{title}"
price: "{row.get('price', '查看詳情')}"
summary: "{summary}"
rating: "{row.get('rating', '4.5')}"
reviews: "{row.get('reviews', '100+')}"
tags: {tag_list}
filename: "{clean_fname}"
---
{summary}
"""
                with open(filepath, 'w', encoding='utf-8') as wf:
                    wf.write(content)
        print("✨ 網頁檔案產生完成，數據已清理。")
    except Exception as e:
        print(f"❌ 錯誤: {e}")

if __name__ == "__main__": generate_safe_posts()