import csv
import os
from datetime import datetime
import requests
import json
import time

# --- 設定區 ---
API_KEY = "AIzaSyB7c1lrLpOGWwx6R9N0KJVTM0yGMRtgqn4"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

if not os.path.exists('_posts'):
    os.makedirs('_posts')
else:
    for file in os.listdir('_posts'):
        if file.endswith('.md'):
            os.remove(os.path.join('_posts', file))

today = datetime.now().strftime('%Y-%m-%d')

def ask_ai_via_rest(keyword):
    """
    呼叫 AI 並增加錯誤保護機制
    """
    print(f"🤖 AI 正在為 '{keyword}' 生成文案...")
    prompt = f"你是一個電商專家。請針對 '{keyword}' 寫一段 50 字內的繁體中文優惠摘要，並給一個簡短標語。格式：摘要|標語"
    
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    
    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        data = response.json()
        
        # 檢查回傳是否有內容
        if 'candidates' in data and data['candidates'][0]['content']['parts'][0]['text']:
            text = data['candidates'][0]['content']['parts'][0]['text'].strip()
            if '|' in text:
                s, p = text.split('|', 1)
                return s.strip(), p.strip()
            return text, "立即查看"
    except Exception as e:
        print(f"⚠️ AI 暫時無法回應，使用保底模板...")
    
    # --- 智慧保底模板 (當 AI 失敗時自動執行) ---
    templates = {
        "KFC": ("2025 肯德基激省優惠碼！包含蛋塔、炸雞個人餐與多人分享餐隱藏代碼，實測可用。", "激省 5 折起"),
        "PIZZAHUT": ("必勝客 Pizza Hut 限時優惠！外帶大比薩買一送一，最新隱藏優惠碼全收錄。", "買一送一起"),
        "DEFAULT": (f"精選 {keyword} 2025 最新優惠，包含限時折扣碼與領取教學，立即點擊查看。", "領券省更多")
    }
    
    # 根據關鍵字選擇模板
    for k in templates:
        if k in keyword.upper():
            return templates[k]
    return templates["DEFAULT"]

# --- 處理 CSV ---
try:
    with open('products.csv', mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        reader.fieldnames = [name.strip() for name in reader.fieldnames]
        
        count = 0
        for row in reader:
            row = {k.strip(): v.strip() for k, v in row.items() if k}
            fname = row.get('filename')
            if not fname: continue
            
            title = row.get('title')
            if not title:
                title = fname.split('-')[0].upper()
            
            summary = row.get('summary', '')
            price = row.get('price', '')

            # 如果內容空白或太短，啟動 AI/模板補完
            if len(summary) < 5 or not price:
                ai_s, ai_p = ask_ai_via_rest(title)
                summary = ai_s if len(summary) < 5 else summary
                price = price if not price else price
                time.sleep(0.5)
            
            filename = f"{today}-{fname.replace('.md', '')}.md"
            filepath = os.path.join('_posts', filename)
            
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

**[👉 點此前往官方活動頁面]({row.get('affiliate_link', '#')})**
"""
            with open(filepath, 'w', encoding='utf-8') as wf:
                wf.write(content)
            count += 1
            
        print(f"\n✨ 任務完成！共更新 {count} 篇商品檔案。")

except Exception as e:
    print(f"❌ 發生錯誤：{e}")