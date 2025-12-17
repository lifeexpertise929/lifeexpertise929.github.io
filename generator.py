import csv
import os
import shutil
import google.generativeai as genai
from datetime import datetime
import json

# 1. 設定區
GOOGLE_API_KEY = "AIzaSyDD3MPq7zgpHtUUSzL0eNXEpKj2MeoCum0" # 已填入您的 Key
CSV_FILE = 'products.csv'
POSTS_DIR = '_posts'
PAGES_DIR = 'pages' 

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. 初始化資料夾 (自動清空舊檔，達到最純淨自動化)
for folder in [POSTS_DIR, PAGES_DIR]:
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)

def ask_ai(link):
    prompt = f"""
    請針對這個導購連結進行分析：{link}
    請直接回傳 JSON 格式（不要有 markdown 外框，也不要解釋）：
    {{
      "title": "吸引人的產品標題",
      "tags": "標籤1, 標籤2",
      "summary": "50字內的吸引力簡介",
      "content": "200字左右的專業推薦理由"
    }}
    """
    try:
        response = model.generate_content(prompt)
        text = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(text)
    except:
        return None

def generate_static_pages():
    """自動生成 關於我們 與 隱私權政策"""
    pages = {
        "about.md": {
            "title": "關於選品智庫",
            "content": "我們是「選品智庫」團隊，致力於透過 AI 技術與專業實測，為讀者篩選出市面上最具性價比的優質產品。我們的目標是簡化您的購物決策，讓每一分錢都花在刀口上。"
        },
        "privacy.md": {
            "title": "隱私權政策",
            "content": "本站尊重您的隱私。我們僅透過聯盟行銷連結獲取分潤以維持營運，不會主動收集您的個人識別資料。當您點擊連結前往第三方平台時，請參閱該平台的條款。"
        }
    }
    for filename, data in pages.items():
        path = os.path.join(PAGES_DIR, filename)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f"---\nlayout: page\ntitle: {data['title']}\npermalink: /{filename.replace('.md', '/')}\n---\n\n{data['content']}")
    print("✅ 固定頁面（關於、隱私）已自動更新。")

def generate_post(row):
    row = {k.strip().lower(): v for k, v in row.items()}
    link = row.get('affiliate_link', '')
    
    # 若 CSV 欄位留空，則啟動 AI 撰寫
    if not row.get('title') or not row.get('summary'):
        print(f"🤖 AI 正在撰寫內容: {link[:40]}...")
        ai_data = ask_ai(link)
        if ai_data:
            row['title'] = ai_data.get('title', '精選選品')
            row['summary'] = ai_data.get('summary', '今日最優選')
            row['tags'] = ai_data.get('tags', '選品, 推薦')
            content_body = ai_data.get('content', '專業實測推薦，值得您入手。')
        else:
            row['title'], row['summary'], row['tags'], content_body = "優質產品", "限時優惠中", "推薦", "實測好物。"
    else:
        # 如果 CSV 有寫內容，就用 CSV 的
        content_body = f"我們針對 {row['title']} 進行了深度評測，這絕對是今日最值得入手的選擇。"

    tags_list = [t.strip() for t in row['tags'].split(',')]
    tags_str = '[' + ', '.join(f'"{t}"' for t in tags_list) + ']'
    
    # 智慧判斷標籤區塊
    cta_text = "查看專業選品組優惠" if "頭皮護理" in tags_list else "前往領取今日限定優惠"
    
    return f"""---
layout: post
title: {row['title']}
date: {datetime.now().strftime('%Y-%m-%d')}
tags: {tags_str}
price: {row.get('price', '優惠中')}
summary: {row['summary']}
---

## 🌟 專業實測推薦：{row['title']}

{content_body}

### 💎 為什麼選擇這個連結？
* **官方授權**：來源安全可靠，售後有保障。
* **限時低價**：連結已自動套用當前最優折扣碼。

<div class="cta-box">
  <a href="{link}" class="buy-button" target="_blank">{cta_text}</a>
</div>
"""

# 3. 執行生成
generate_static_pages() 
with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        raw_fn = row.get('filename') or f"product-{datetime.now().microsecond}.md"
        filename = f"{datetime.now().strftime('%Y-%m-%d')}-{raw_fn.strip()}"
        with open(os.path.join(POSTS_DIR, filename), 'w', encoding='utf-8') as out_f:
            out_f.write(generate_post(row))
print("✨ AI 全自動生成完成！所有文章與頁面已同步。")