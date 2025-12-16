---
layout: default
title: 歡迎來到 頭皮智庫 (Scalp Think Tank)
---

# 歡迎來到 頭皮智庫 (Scalp Think Tank)

我們的核心使命
: 頭皮智庫是您的專業頭皮健康顧問。我們自動化彙整與分析市場上所有養護產品、技術與趨勢，為您提供：
* 最客觀的產品比較清單。
* 最有效的頭皮問題（掉髮、出油、敏感）解決方案。
* 最即時的聯盟行銷產品推薦。

## 產品清單 (Product Review List)

<div class="product-list">
{% assign products = site.data.products %}
{% for product in products %}
    <div class="product-item">
        <h3 class="product-title">
            <a href="/products/{{ product.filename | remove_first: '.md' }}">
                {{ product.title }}
            </a>
        </h3>
        <p class="product-summary">{{ product.summary }}</p>
        <div class="product-meta">
            <span class="price">💰 價格: NT${{ product.price }}</span>
            <span class="tags">標籤: 
                {% for tag in product.tags %}
                    <span class="tag-item">{{ tag }}</span>{% unless forloop.last %}, {% endunless %}
                {% endfor %}
            </span>
        </div>
        <a href="/products/{{ product.filename | remove_first: '.md' }}" class="read-more-button">閱讀完整評測</a>
    </div>
{% endfor %}
</div>

## 立即解決您的頭皮困擾！

點擊下方連結了解我們如何幫助您：

* [關於我們](about.md)
* [隱私權政策](privacy.md)