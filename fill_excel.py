import pandas as pd
import numpy as np

file_path = 'products.csv'

def final_fix():
    print("🚀 啟動終極填充引擎...")
    
    try:
        # 1. 讀取並強行清除所有欄位名稱的前後空白
        df = pd.read_csv(file_path, encoding='utf-8-sig')
        df.columns = [c.strip() for c in df.columns]
        
        # 2. 定義知識庫 (關鍵字包含你的檔名特徵)
        kb = {
            "pizzahut": ("🍕 買一送一起", "2025 必勝客隱藏優惠碼：包含外帶買一送一、比薩套餐折價券實測可用。", "4.6", "10萬+ 食客好評"),
            "kfc": ("🍗 激省 5 折起", "肯德基激省代碼大全：炸雞、蛋塔、個人餐通通有優惠，實測代碼可用。", "4.5", "8萬+ 用戶推薦"),
            "klook": ("✈️ 現折 $100", "KLOOK 全球旅遊優惠碼：包含國外景點門票、交通票券隱藏折扣。", "4.8", "60萬+ 旅人好評"),
            "kkday": ("✈️ 滿額折 $100", "2025 旅遊必備 KKDAY 優惠清單，包含全球一日遊體驗與機場接送折扣。", "4.7", "30萬+ 旅人推薦"),
            "shoppee": ("🎁 免運優惠中", "蝦皮購物 2025 免運券、折價券領取攻略。包含商城折扣碼與限時特賣資訊。", "4.8", "200萬+ 買家推薦"),
            "yahoo": ("💰 領券折 15%", "YAHOO 購物中心領券教學：隱藏版 15% 回饋領取流程實測。", "4.4", "15萬+ 會員評鑑"),
            "carrefour": ("🛒 滿額折 $100", "家樂福線上購物免排隊！輸入折扣碼現折 $100，當日配送超方便。", "4.2", "5萬+ 用戶好評"),
            "agoda": ("🏨 訂房 9 折起", "Agoda 全球訂房優惠：隱藏版特惠折扣碼，實測國內外住宿皆適用。", "4.6", "200萬+ 旅人好評")
        }

        # 3. 逐行處理
        for index, row in df.iterrows():
            # 優先用 filename 或 title 來比對關鍵字
            search_text = (str(row.get('filename', '')) + str(row.get('title', ''))).lower()
            
            for key, val in kb.items():
                if key in search_text:
                    # 針對你的 CSV 欄位填入資料
                    # 欄位：price, summary, rating, badge
                    if pd.isna(df.at[index, 'price']) or str(df.at[index, 'price']).strip() in ['', 'nan']:
                        df.at[index, 'price'] = val[0]
                    if pd.isna(df.at[index, 'summary']) or str(df.at[index, 'summary']).strip() in ['', 'nan']:
                        df.at[index, 'summary'] = val[1]
                    if pd.isna(df.at[index, 'rating']) or str(df.at[index, 'rating']).strip() in ['', 'nan']:
                        df.at[index, 'rating'] = val[2]
                    if pd.isna(df.at[index, 'badge']) or str(df.at[index, 'badge']).strip() in ['', 'nan']:
                        df.at[index, 'badge'] = val[3]
                    break

        # 4. 儲存檔案並強制使用 utf-8-sig
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print("✨ [大功告成] Excel 已經強行寫入成功！")
        
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")

if __name__ == "__main__":
    final_fix()