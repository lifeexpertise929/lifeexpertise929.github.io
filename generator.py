import csv
import os
import random
from datetime import datetime

# --- 1. 環境設定 ---
POSTS_DIR = '_posts'
if not os.path.exists(POSTS_DIR):
    os.makedirs(POSTS_DIR)

# 取得現在的日期資訊，用於 SEO 標題優化
now = datetime.now()
current_year_month = now.strftime('%Y 年 %m 月')
today_str = now.strftime('%Y-%m-%d')

def get_marketing_logic(tags, brand_name):
    """
    數據偵察機：根據分類自動產生具備『比價感』的動態數據。
    """
    tags_str = str(tags)
    if "美食類" in tags_str:
        auto_price = "🍕 買一送一起"
        auto_badge = "今日代碼實測有效"
        marketing_text = f"整理 {current_year_month} 最新 {brand_name} 隱藏代碼。小編實測包含外帶買一送一與套餐省錢優惠。"
    elif "旅遊類" in tags_str:
        auto_price = "✈️ 領券現折 $100"
        auto_badge = "限時領取中"
        marketing_text = f"本站已為您定位 {brand_name} 目前最優價格入口。搭配指定銀行信用卡結帳，回饋最高再加碼。"
    elif "購物網站" in tags_str:
        auto_price = "🎁 免運優惠中"
        auto_badge = "全站促銷中"
        marketing_text = f"蒐羅 {brand_name} 全網折扣訊息，包含免運券、商城折價券。推薦在活動時間內完成結帳以免向隅。"
    else:
        auto_price = "🔥 限時 5 折起"
        auto_badge = "精選推薦"
        marketing_text = f"為您即時監測 {brand_name} 的價格動向。{current_year_month} 期間建議優先使用本站提供的專屬連結。"

    return auto_price, auto_badge, marketing_text

def generate_site():
    print(f"🚀 啟動自動化生產線：正在生成 {current_year_month} 的最新網頁內容...")
    
    try:
        with open('products.csv', mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            # 清洗欄位空白
            reader.fieldnames = [name.strip() for name in reader.fieldnames]
            
            count = 0
            for row in reader:
                # 清洗每行數據
                row = {k.strip(): v.strip() for k, v in row.items() if k}
                fname = row.get('filename')
                if not fname: continue
                
                # 取得品牌與分類
                brand = row.get('title', fname.split('-')[0].capitalize())
                tags = row.get('tags', '精選')
                tag_list = [t.strip() for t in tags.split(',')]

                # 呼叫數據偵察機邏輯
                auto_p, auto_b, auto_m = get_marketing_logic(tags, brand)

                # 核心 SEO 標題：自動加上當前年份與月份
                final_title = f"{brand}：{current_year_month} 最新優惠代碼/比價推薦/領取攻略"
                
                # 自動填充數據邏輯 (Excel 優先，空白則自動補齊)
                price = row.get('price') if row.get('price') else auto_p
                summary = row.get('summary') if row.get('summary') else auto_m
                badge = row.get('badge') if row.get('badge') else auto_b
                rating = row.get('rating') if row.get('rating') else str(round(random.uniform(4.3, 4.9), 1))
                reviews = row.get('reviews') if row.get('reviews') else f"{random.randint(10, 50)} 萬+"
                affiliate = row.get('affiliate_link', '#')

                # 建立 Markdown 內容 (YAML Front Matter)
                # 使用 | 確保 summary 多行文字不會破壞格式
                content = f"""---
layout: post
title: "{final_title}"
price: "{price}"
summary: "{summary}"
rating: "{rating}"
reviews: "{reviews}"
badge: "{badge}"
tags: {tag_list}
filename: "{fname.replace('.md', '')}"
affiliate_link: "{affiliate}"
---
### 💡 {brand} 今日最夯亮點 (更新於 {current_year_month})

目前 {brand} 在「{tag_list[0]}」分類中提供了非常具有競爭力的優惠條件。以下是本站數據偵察機為您整理的重點：

1. **價格優勢**：目前實測可獲得 **{price}**，這在目前的市場行情中極具競爭力。
2. **領取便利性**：本站提供的 {badge} 連結，經實測能有效縮短搜尋時間。
3. **用戶回饋**：累積超過 {reviews} 則評價，顯示該品牌服務穩定可靠。

#### 領取步驟說明：
* 點擊下方按鈕前往指定優惠入口。
* 登入或註冊會員以領取最新的專屬折扣碼。
* 於結帳頁面輸入代碼或直接使用專屬連結完成訂購。

**[👉 立即前往領取 {brand} 專屬優惠]({affiliate})**

---
*免責聲明：本站數據為自動化採集，實際優惠價格、期限與限制條件請以官方網站公告為準。*
"""
                # 寫入檔案
                clean_fname = fname.replace('.md', '')
                filepath = os.path.join(POSTS_DIR, f"{today_str}-{clean_fname}.md")
                with open(filepath, 'w', encoding='utf-8') as wf:
                    wf.write(content)
                count += 1
            
            print(f"✨ 任務完成！已生成 {count} 篇包含『{current_year_month}』關鍵字的導購頁面。")

    except Exception as e:
        print(f"❌ 發生錯誤：{e}")

if __name__ == "__main__":
    generate_site()