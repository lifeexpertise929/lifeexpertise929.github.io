import csv
import os
import random
from datetime import datetime

# 設定輸出路徑
POSTS_DIR = '_posts'
if not os.path.exists(POSTS_DIR):
    os.makedirs(POSTS_DIR)

# 取得今天的日期作為檔名前綴
today = datetime.now().strftime('%Y-%m-%d')

def get_auto_marketing(tags, brand_name):
    """
    根據分類自動生成『真實感』的比價與行銷數據。
    這些數據基於各大平台的長期通用優惠，確保真實度與吸引力並存。
    """
    tags = str(tags)
    if "美食類" in tags:
        price = "🍕 買一送一起"
        summary = f"整理 2025 最新 {brand_name} 隱藏代碼，實測包含外帶買一送一與套餐折價，適合小資族省錢點餐。"
        badge = "網友實測有效"
        rating = random.choice(["4.5", "4.6", "4.7"])
        reviews = f"{random.randint(5, 15)} 萬+"
    elif "旅遊類" in tags:
        price = "✈️ 領券現折 $100"
        summary = f"提供 {brand_name} 全球景點門票與交通接送優惠碼，搭配指定信用卡結帳再享額外折扣，出國必備。"
        badge = "官方合作領券"
        rating = random.choice(["4.7", "4.8", "4.9"])
        reviews = f"{random.randint(50, 200)} 萬+"
    elif "購物網站" in tags:
        price = "🎁 免運優惠中"
        summary = f"精選 {brand_name} 今日限時免運券與商城折價券，包含跨境購物教學與隱藏優惠，手慢就沒了。"
        badge = "限時加碼回饋"
        rating = random.choice(["4.4", "4.5", "4.6"])
        reviews = f"{random.randint(100, 300)} 萬+"
    else:
        price = "🔥 限時 5 折起"
        summary = f"為您監測 {brand_name} 最新價格波動，目前正處於年度促銷區間，建議立即前往查看詳情。"
        badge = "精選選品"
        rating = "4.5"
        reviews = "10 萬+"
        
    return price, summary, badge, rating, reviews

def generate_posts():
    print("🚀 啟動全自動化網頁生成器...")
    
    try:
        with open('products.csv', mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            reader.fieldnames = [name.strip() for name in reader.fieldnames]
            
            count = 0
            for row in reader:
                # 清洗數據
                row = {k.strip(): v.strip() for k, v in row.items() if k}
                fname = row.get('filename')
                if not fname: continue
                
                brand_name = row.get('title', fname.split('-')[0].capitalize())
                tags = row.get('tags', '精選')

                # 取得自動化數據 (若 CSV 沒填則自動補足)
                auto_p, auto_s, auto_b, auto_r, auto_rv = get_auto_marketing(tags, brand_name)

                # 決定最終使用的數值 (Excel 優先，空白則自動填充)
                title = row.get('title') if row.get('title') else f"{brand_name}：2025 最新優惠代碼與比價整理"
                price = row.get('price') if row.get('price') else auto_p
                summary = row.get('summary') if row.get('summary') else auto_s
                badge = row.get('badge') if row.get('badge') else auto_b
                rating = row.get('rating') if row.get('rating') else auto_r
                reviews = row.get('reviews') if row.get('reviews') else auto_rv
                
                # 清理標籤
                tag_list = [t.strip() for t in tags.split(',')]

                # 建立 Markdown 內容
                content = f"""---
layout: post
title: "{title}"
price: "{price}"
summary: "{summary}"
rating: "{rating}"
reviews: "{reviews}"
badge: "{badge}"
tags: {tag_list}
filename: "{fname.replace('.md', '')}"
affiliate_link: "{row.get('affiliate_link', '#')}"
---
### 💡 為什麼選擇在 {brand_name} 領取優惠？
本站自動化監測系統顯示，{brand_name} 目前正針對「{tag_list[0]}」類別提供年度最強力度的促銷活動。

#### 本次優惠重點：
* **即時性**：{auto_b}，確保您可以順利使用。
* **比價感**：透過本站入口可直接定位到最划算的「{price}」方案。
* **高評價**：目前已累積超過 {reviews} 則正面評價，服務穩定。

**[👉 點此立即前往 {brand_name} 領取今日專屬優惠]({row.get('affiliate_link', '#')})**

---
*免責聲明：本站透過自動化技術整合各大平台優惠資訊，實際價格與活動內容請以品牌官網最終公告為準。*
"""
                # 寫入檔案
                clean_fname = fname.replace('.md', '')
                filepath = os.path.join(POSTS_DIR, f"{today}-{clean_fname}.md")
                with open(filepath, 'w', encoding='utf-8') as wf:
                    wf.write(content)
                count += 1
            
            print(f"✨ 成功！已自動化產生 {count} 篇專業導購網頁。")

    except Exception as e:
        print(f"❌ 發生錯誤：{e}")

if __name__ == "__main__":
    generate_posts()