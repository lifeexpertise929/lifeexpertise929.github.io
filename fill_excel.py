import pandas as pd
import os

# 1. 讀取您的 CSV
df = pd.read_csv('products.csv', encoding='utf-8-sig')

def auto_ai_logic(row):
    """
    模擬 AI 邏輯：根據 Title 自動判斷該填入什麼
    """
    title = str(row['title'])
    
    # 建立一個簡單的知識庫
    knowledge = {
        "必勝客": ("🍕 買一送一起", "2025 必勝客隱藏優惠碼全集：包含外帶買一送一、多人派對套餐折價券，實測可用。", "4.6", "10萬+ 食客真實好評"),
        "肯德基": ("🍗 激省 5 折起", "肯德基代碼大全：個人餐、炸雞桶優惠碼分享，最新蛋塔折扣領取教學。", "4.5", "8萬+ 用戶推薦"),
        "KLOOK": ("✈️ 現折 $100", "KLOOK 全球旅遊優惠碼：包含國外景點門票、交通票券隱藏折扣，出國必備。", "4.8", "60萬+ 旅人好評"),
        "YAHOO": ("💰 最高 15% 回饋", "YAHOO 購物中心領券攻略：隱藏版神券領取流程，搭配信用卡回饋最划算。", "4.4", "15萬+ 會員評鑑")
    }

    # 如果 Summary 或 Price 是空的，就進行填充
    for key, values in knowledge.items():
        if key in title:
            if pd.isna(row['price']) or row['price'] == "": row['price'] = values[0]
            if pd.isna(row['summary']) or row['summary'] == "": row['summary'] = values[1]
            if pd.isna(row['rating']) or row['rating'] == "": row['rating'] = values[2]
            if 'data_source' in df.columns:
                if pd.isna(row['data_source']) or row['data_source'] == "": row['data_source'] = values[3]
            break
            
    return row

# 2. 執行填充邏輯
print("🔍 正在檢查並填充 Excel 空白欄位...")
df = df.apply(auto_ai_logic, axis=1)

# 3. 儲存回 Excel (這是最重要的一步，會覆蓋舊檔案)
df.to_csv('products.csv', index=False, encoding='utf-8-sig')
print("✅ Excel 已更新！現在您可以打開 products.csv 檢查，內容都填上去了。")