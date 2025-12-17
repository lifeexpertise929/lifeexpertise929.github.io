---
layout: default
title: 選品智庫 - AI 驅動的極致省錢術
---

<style>
  /* 讓版面自動變為網格，解決「一直往下拉」的問題 */
  .post-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 15px;
    margin-top: 20px;
  }

  .post-card {
    background: #ffffff;
    border: 1px solid #eaeaea;
    border-radius: 8px;
    padding: 16px;
    transition: all 0.2s ease;
    display: flex;
    flex-direction: column;
    text-decoration: none !important;
    color: inherit !important;
  }

  .post-card:hover {
    border-color: #d32f2f;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  }

  .post-card-title {
    font-size: 1.1rem;
    font-weight: bold;
    color: #d32f2f;
    margin-bottom: 8px;
    line-height: 1.3;
  }

  .post-card-summary {
    font-size: 0.85rem;
    color: #666;
    margin-bottom: 12px;
    flex-grow: 1;
    display: -webkit-box;
    -webkit-line-clamp: 2; /* 限制摘要顯示兩行，保持整齊 */
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .post-card-price {
    font-size: 0.8rem;
    color: #f57c00;
    font-weight: bold;
    border-top: 1px dashed #eee;
    padding-top: 10px;
  }
</style>

# 📌 最新選品推薦

<div class="post-grid">
  {% for post in site.posts %}
  <a href="{{ post.url }}" class="post-card">
    <div class="post-card-title">{{ post.title }}</div>
    <div class="post-card-summary">{{ post.summary }}</div>
    <div class="post-card-price">🏷️ {{ post.price }}</div>
  </a>
  {% endfor %}
</div>