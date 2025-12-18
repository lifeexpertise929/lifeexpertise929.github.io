import csv
import os
from datetime import datetime
import google.generativeai as genai
import time

# --- 1. AI 核心設定 ---
# 使用您提供的 API Key
genai.configure(api_key="AIzaSyB7c1lrLpOGWwx6R9N0KJVTM0yGMRtgqn4")

# 修正：使用基礎模型路徑，這在目前的 API 版本中最穩定
model = genai.GenerativeModel('models/gemini-1.5-flash')

# 確保輸出目錄存在
if not os.path.exists('_posts'):
    os.makedirs('_posts')
else:
    # 每次執行前清空舊檔案，確保資料與 CSV 同步
    for file in os.listdir('_posts'):
        if file.endswith('.md'):
            os.remove(os.path.join('_posts', file))

today = datetime.now().strftime('%Y-%m-%d')

def ask_ai_for_content(keyword):
    """
    當內容缺失時，根據標題或關鍵字召喚 AI 生成文案
    """
    print(f"🤖 AI 正在為 '{keyword}' 抓取並自動生成文案...")
    # 明確定義輸出格式，方便程式解析
    prompt = f"你是一個專業電商小編。請針對 '{keyword}' 提供一段 60 字內的繁體中文優惠摘要，並提供一個短價格標語（如：買一送一、激省 5 折起）。請務必用 '|' 分隔，格式如下：摘要|標語"
    
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        
        # 解析 AI 回傳的「摘要|標語」格式
        if '|' in text:
            s, p = text.split('|', 1)
            return s.strip(), p.strip()
        return text, "立即查看"
    except Exception as e:
        # 如果 API 還是報錯，提供保底文案，確保網頁不留白
        print(f"❌ AI 生成失敗: {e}")
        return f"精選 {keyword} 2025 最新優惠活動，包含限時折扣碼與領取教學，立即點擊查看詳情。", "領券省更多"

# --- 2. 讀取 CSV 並產生網頁檔案 ---
try:
    with open('products.csv', mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        # 清理標題欄位空白
        reader.fieldnames = [name.strip() for name in reader.fieldnames]
        
        count = 0
        for row in reader:
            # 清理資料內容空白
            row = {k.strip(): v.strip() for k, v in row.items() if k}
            
            fname = row.get('filename')
            if not fname: continue # 沒檔名就跳過
            
            # --- 智慧標題偵測 ---
            title = row.get('title')
            if not title or title == "":
                # 如果標題空了，從檔名推測 (例如 kfc-001.md -> KFC)
                title = fname.split('-')[0].replace('.md', '').upper()
            
            summary = row.get('summary', '')
            price = row.get('price', '')

            # --- 自動補全邏輯：如果摘要太短或價格空白就啟動 AI ---
            if len(summary) < 5 or not price:
                ai_s, ai_p = ask_ai_for_content(title)
                # 只有在原本沒資料時才用 AI 的
                if len(summary) < 5: summary = ai_s
                if not price: price = ai_p
                # 延遲 1 秒，符合免費版 API 頻率限制
                time.sleep(1)
            
            # 建立 Jekyll 格式的檔名
            clean_fname = fname.replace('.md', '')
            filename = f"{today}-{clean_fname}.md"
            filepath = os.path.join('_posts', filename)
            
            # 寫入 Markdown 內容
            content = f"""---
layout: post
title: "{title}"
price: "{price}"
summary: "{summary}"
rating: "{row.get('rating', '4.8')}"
data_source: "{row.get('data_source', 'AI 數據監測')}"
tags: [{row.get('tags', '精選優惠')}]
---
### {title} 2025 最新折扣情報
{summary}

想要獲取更多隱藏優惠碼？
**[👉 點此前往官方活動頁面]({row.get('affiliate_link', '#')})**
"""
            with open(filepath, 'w', encoding='utf-8') as wf:
                wf.write(content)
            count += 1
            
        print(f"\n✨ 任務完成！共更新 {count} 篇商品檔案，空白處已自動補全。")

except Exception as e:
    print(f"❌ 發生錯誤：{e}")