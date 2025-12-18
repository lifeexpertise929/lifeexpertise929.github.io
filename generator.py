import csv
import os
from datetime import datetime
import requests
import json
import time

# --- 1. 設定區 ---
API_KEY = "AIzaSyB7c1lrLpOGWwx6R9N0KJVTM0yGMRtgqn4"
# 使用 Google 的 REST API 網址，這最穩定
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
    使用 REST API 直接呼叫 AI，解決套件 404 問題
    """
    print(f"🤖 AI 正在為 '{keyword}' 生成文案...")
    prompt = f"你是一個專業電商小編。請針對 '{keyword}' 提供一段 60 字內的繁體中文優惠摘要，並提供一個價格標語（如：買一送一）。格式：摘要|標語"
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    try:
        response = requests.post(API_URL, json=payload, headers={'Content-Type': 'application/json'})
        data = response.json()
        # 解析回傳內容
        text = data['candidates'][0]['content']['parts'][0]['text'].strip()
        
        if '|' in text:
            s, p = text.split('|', 1)
            return s.strip(), p.strip()
        return text, "立即查看"
    except Exception as e:
        print(f"❌ AI 連線失敗: {e}")
        return f"精選 {keyword} 2025 最新優惠，包含限時折扣碼與領取教學。", "領券省更多"

# --- 2. 處理 CSV ---
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

            # 如果內容空白，就呼叫 AI
            if len(summary) < 5 or not price:
                ai_s, ai_p = ask_ai_via_rest(title)
                summary = ai_s if len(summary) < 5 else summary
                price = price if not price else price
                time.sleep(1) # 避開限制
            
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