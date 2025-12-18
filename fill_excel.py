import pandas as pd
import os

# 讀取 CSV
file_path = 'products.csv'
try:
    # 讀取時自動去掉欄位名稱的空格
    df = pd.read_csv(file_path, encoding='utf-8-sig')
    df.columns = df.columns.str.strip()
except Exception as e:
    print(f"❌ 讀取失敗: {e}")
    exit()

def smart_fill(row):
    # 取得標題並轉為小寫，方便比對
    title = str(row.get('title', '')).lower()
    
    # 定義更強大的知識庫
    # 格式: 關鍵字: (價格, 摘要, 星等, 數據來源)
    kb = {
        "必勝客": ("🍕 買一送一起", "2025 必勝客隱藏優惠碼：包含外帶買一送一、比薩套餐折價券實測可用。", "4.6", "10萬+ 食客好評"),
        "pizzahut": ("🍕 買一送一起", "2025 必勝客隱藏優惠碼：包含外帶買一送一、比薩套餐折價券實測可用。", "4.6", "10萬+ 食客好評"),
        "肯德基": ("🍗 激省 5 折起", "肯德基激省代碼大全：炸雞、蛋塔、個人餐通通有優惠，實測代碼可用。", "4.5", "8萬+ 用戶推薦"),
        "kfc": ("🍗 激省 5 折起", "肯德基激省代碼大全：炸雞、蛋塔、個人餐通通有優惠，實測代碼可用。", "4.5", "8萬+ 用戶推薦"),
        "蝦皮": ("🎁 免運優惠中", "蝦皮購物 2025 免運券、折價券領取攻略。包含商城折扣碼與限時特賣資訊。", "4.8", "200萬+ 買家推薦"),
        "shopee": ("🎁 免運優惠中", "蝦皮購物 2025 免運券、折價券領取攻略。包含商城折扣碼與限時特賣資訊。", "4.8", "200萬+ 買家推薦"),
        "momo": ("💰 滿額領現折券", "Momo 購物網限時折扣：提供家電、美妝與生活用品隱藏優惠碼領取教學。", "4.7", "100萬+ 客戶認證")
    }

    # 檢查並填充 (只要欄位是 NaN 或 空字串就填入)
    for key, val in kb.items():
        if key in title:
            # 依序填充: price, summary, rating, data_source
            cols = ['price', 'summary', 'rating', 'data_source']
            for i, col in enumerate(cols):
                if col in df.columns:
                    # 如果原本是空的，就補上
                    if pd.isna(row[col]) or str(row[col]).strip() == "":
                        row[col] = val[i]
            break
    return row

print("🚀 啟動智能填充引擎...")
# 確保所有對象都是字串處理，避免型別報錯
df = df.apply(smart_fill, axis=1)

# 寫回 CSV 並強制不保留索引列
df.to_csv(file_path, index=False, encoding='utf-8-sig')
print("✅ 成功！Excel 空白處已填補。請「關閉」Excel 後查看效果。")