import csv
import os
from datetime import datetime

# 設定輸出資料夾
POSTS_DIR = '_posts'
if not os.path.exists(POSTS_DIR):
    os.makedirs(POSTS_DIR)

# 取得今天的日期作為檔名前綴
today = datetime.now().strftime('%Y-%m-%d')

def generate_posts():
    print("🔨 正在從 CSV 產生網頁 Markdown 檔案...")
    
    try:
        # 使用 utf-8-sig 處理 Excel 可能產生的 BOM
        with open('products.csv', mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            
            # 清洗欄位名稱，避免空白字元干擾
            reader.fieldnames = [name.strip() for name in reader.fieldnames]
            
            count = 0
            for row in reader:
                # 清洗每一列的數據
                row = {k.strip(): v.strip() for k, v in row.items() if k}
                
                # 取得必要資訊
                fname = row.get('filename')
                if not fname:
                    continue
                
                # 處理標籤邏輯：第一個詞作為主要分類 (Category)
                raw_tags = row.get('tags', '精選選品')
                tag_list = [t.strip() for t in raw_tags.split(',')]
                main_category = tag_list[0] if tag_list else "精選選品"
                
                # 清理檔名，移除 .md 後綴 (避免重複)
                clean_fname = fname.replace('.md', '')
                final_filename = f"{today}-{clean_fname}.md"
                filepath = os.path.join(POSTS_DIR, final_filename)
                
                # 建立 Markdown 內容 (YAML Front Matter)
                # 包含你剛補齊的 reviews, badge, rating 等欄位
                content = f"""---
layout: post
title: "{row.get('title', '限時優惠')}"
price: "{row.get('price', '立即查看')}"
summary: "{row.get('summary', '')}"
rating: "{row.get('rating', '4.5')}"
reviews: "{row.get('reviews', '100+')}"
badge: "{row.get('badge', '官方推薦')}"
category: "{main_category}"
tags: {tag_list}
filename: "{clean_fname}"
affiliate_link: "{row.get('affiliate_link', '#')}"
---
### 優惠詳情介紹
{row.get('summary', '最新優惠資訊整理中，請點擊下方按鈕查看詳情。')}

**[👉 點此前往領取最新優惠碼]({row.get('affiliate_link', '#')})**

---
*本網頁資訊最後更新於：{today}。實際優惠內容以官方網站公告為準。*
"""
                # 寫入檔案
                with open(filepath, 'w', encoding='utf-8') as wf:
                    wf.write(content)
                count += 1
            
            print(f"✨ 成功！已在 {POSTS_DIR} 資料夾產生 {count} 篇 Markdown 檔案。")

    except FileNotFoundError:
        print("❌ 錯誤：找不到 products.csv 檔案，請確認檔案是否存在。")
    except Exception as e:
        print(f"❌ 發生未知錯誤：{e}")

if __name__ == "__main__":
    generate_posts()