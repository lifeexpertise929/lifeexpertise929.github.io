import json
import os

# 1. 定義路徑
DATA_FILE = '_data/products.json'
OUTPUT_DIR = 'products'
TEMPLATE = """---
layout: post
title: {title}
date: {date}
tags: {tags}
price: {price}
summary: {summary}
{affiliate_link_line}
---

這是 {title} 的詳細評測文章。請在 {filename} 檔案中填寫內容。

## 產品主要優點

* 溫和不刺激
* 有效控油
* 專業醫師推薦

## 使用心得與建議

請在此處填寫產品的實際使用體驗、成分分析和購買建議。
"""

# 2. 確保輸出資料夾存在
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# 3. 載入產品數據
try:
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        products = json.load(f)
except FileNotFoundError:
    print(f"錯誤：找不到資料檔案 {DATA_FILE}。請確認 products.json 位於 _data 資料夾中。")
    exit()
except json.JSONDecodeError:
    print(f"錯誤：{DATA_FILE} 檔案格式錯誤。請檢查 JSON 語法。")
    exit()

# 4. 生成 Markdown 文件
for product in products:
    filename = product.get('filename')
    title = product.get('title', '無標題')
    
    if not filename:
        print(f"警告：產品 {title} 缺少 filename 欄位，跳過生成。")
        continue

    output_path = os.path.join(OUTPUT_DIR, filename)

    # 處理標籤格式
    tags_list = product.get('tags', [])
    tags_string = '[' + ', '.join(f'"{tag}"' for tag in tags_list) + ']'
    
    # 處理聯盟行銷連結（單一連結或多選項）
    affiliate_options = product.get('affiliate_options')
    affiliate_link = product.get('affiliate_link')
    
    if affiliate_options:
        # 如果是多連結，需要單獨處理這一行
        affiliate_link_line = "affiliate_options: " + json.dumps(affiliate_options, ensure_ascii=False)
    elif affiliate_link:
        # 如果是單連結
        affiliate_link_line = f"affiliate_link: {affiliate_link}"
    else:
        affiliate_link_line = ""
    
    # 填充模板
    content = TEMPLATE.format(
        title=title,
        date=product.get('date', 'YYYY-MM-DD'),
        tags=tags_string,
        price=product.get('price', 'N/A'),
        summary=product.get('summary', '無摘要'),
        filename=filename,
        affiliate_link_line=affiliate_link_line # 僅包含連結或選項的行
    )

    # 寫入文件
    if not os.path.exists(output_path):
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"成功生成新文章：{output_path}")
    else:
        # 如果檔案已存在，則只更新 YAML Front Matter 區塊
        with open(output_path, 'r', encoding='utf-8') as f:
            existing_content = f.read()
        
        # 找到 Front Matter 結束位置
        if existing_content.startswith('---'):
            end_matter = existing_content.find('---', 3)
            if end_matter != -1:
                body = existing_content[end_matter + 3:].lstrip()
                
                # 寫入更新後的 Front Matter 和原有的內容主體
                new_content = TEMPLATE.format(
                    title=title,
                    date=product.get('date', 'YYYY-MM-DD'),
                    tags=tags_string,
                    price=product.get('price', 'N/A'),
                    summary=product.get('summary', '無摘要'),
                    filename=filename,
                    affiliate_link_line=affiliate_link_line
                )
                
                # 移除模板預設的內容主體
                new_content_end = new_content.find('---', 3)
                new_front_matter = new_content[:new_content_end + 3] + '\n'
                
                # 如果 body 已經被修改，則保留 body
                if body.strip() and not body.startswith("這是"):
                    final_content = new_front_matter + body
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(final_content)
                    print(f"成功更新文章 Front Matter：{output_path}")
                else:
                    # 檔案內容是空的或預設內容，保留原模板生成
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"成功更新文章：{output_path} (內容為模板)")

print("所有產品文章已處理完成。")