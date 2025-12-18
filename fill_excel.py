import pandas as pd

file_path = 'products.csv'

def ultimate_sync():
    print("🚀 正在執行全方位數據校準...")
    
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
        df.columns = [c.strip() for c in df.columns]

        # 定義核心分類與知識庫
        # 格式: 關鍵字: (分類標籤, 價格, 摘要, 評分, 勳章)
        kb = {
            "pizzahut": ("美食類", "🍕 買一送一起", "2025 必勝客隱藏優惠碼：包含外帶買一送一、比薩套餐折價券實測可用。", "4.6", "10萬+ 食客好評"),
            "kfc": ("美食類", "🍗 激省 5 折起", "肯德基激省代碼大全：炸雞、蛋塔、個人餐通通有優惠，實測可用。", "4.5", "8萬+ 用戶推薦"),
            "klook": ("旅遊類", "✈️ 現折 $100", "KLOOK 全球旅遊優惠碼：包含國外景點門票、交通票券隱藏折扣。", "4.8", "60萬+ 旅人好評"),
            "kkday": ("旅遊類", "✈️ 滿額折 $100", "2025 旅遊必備 KKDAY 優惠清單，包含全球一日遊體驗與折扣。", "4.7", "30萬+ 旅人推薦"),
            "shoppee": ("購物網站", "🎁 免運優惠中", "蝦皮購物 2025 免運券、折價券領取攻略。包含商城折扣碼資訊。", "4.8", "200萬+ 買家推薦"),
            "yahoo": ("購物網站", "💰 領券折 15%", "YAHOO 購物中心領券教學：隱藏版 15% 回饋領取流程實測。", "4.4", "15萬+ 會員評鑑"),
            "carrefour": ("購物網站", "🛒 滿額折 $100", "家樂福線上購物免排隊！輸入折扣碼現折 $100，當日配送。", "4.2", "5萬+ 用戶好評"),
            "agoda": ("旅遊類", "🏨 訂房 9 折起", "Agoda 全球訂房優惠：隱藏版特惠折扣碼，實測國內外適用。", "4.6", "200萬+ 旅人好評")
        }

        for index, row in df.iterrows():
            filename = str(row.get('filename', '')).lower()
            current_tags = str(row.get('tags', ''))
            
            for key, val in kb.items():
                if key in filename:
                    # 1. 校準 Tags: 確保分類在最前面
                    category = val[0]
                    if category not in current_tags:
                        new_tags = f"{category}, {current_tags.replace('nan', '')}".strip(', ')
                        df.at[index, 'tags'] = new_tags
                    
                    # 2. 補全空白欄位 (Price, Summary, Rating, Badge)
                    mapping = {'price': val[1], 'summary': val[2], 'rating': val[3], 'badge': val[4]}
                    for col, value in mapping.items():
                        if pd.isna(df.at[index, col]) or str(df.at[index, col]).strip() in ['', 'nan']:
                            df.at[index, col] = value
                    break

        # 清洗數據：移除字串中的 nan
        df = df.replace('nan', '', regex=True)
        
        # 儲存
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print("✨ [校準完成] Tags 已分類，內容已補齊！")
        
    except Exception as e:
        print(f"❌ 錯誤: {e}")

if __name__ == "__main__":
    ultimate_sync()