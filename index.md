---
layout: default
title: 選品智庫 - 全球優惠導航
---

<style>
  /* 全域容器設定 */
  .main-content, .container { 
    max-width: 1200px !important; 
    width: 95% !important; 
    margin: 0 auto; 
  }

  /* 頂部橫幅設計 */
  .hero-banner {
    width: 100%; height: 260px;
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('/assets/images/hero-bg.jpg') center/cover no-repeat;
    border-radius: 20px; display: flex; flex-direction: column; align-items: center; justify-content: center;
    color: white; text-align: center; margin-bottom: 40px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  }

  /* 專業網格佈局 */
  .shop-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 25px; padding-bottom: 60px;
  }

  /* 電商感卡片設計 */
  .shop-card {
    background: #ffffff; border-radius: 16px; border: 1px solid #eee;
    overflow: hidden; display: flex; flex-direction: column;
    text-decoration: none !important; transition: all 0.3s ease;
    color: #333 !important;
  }
  .shop-card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.1); border-color: #ff4d4f; }

  /* 核心：圖片偵測邏輯 */
  .card-img {
    width: 100%; height: 180px; background-color: #f9f9f9;
    background-size: contain; background-repeat: no-repeat; background-position: center;
    border-bottom: 1px solid #f0f0f0;
  }

  .card-body { padding: 20px; flex-grow: 1; }
  .card-tag { color: #ff4d4f; font-size: 0.75rem; font-weight: bold; margin-bottom: 8px; display: block; }
  .card-title { font-size: 1.15rem; font-weight: 800; line-height: 1.4; margin-bottom: 10px; color: #111; }
  
  /* 評分樣式修正 */
  .rating-box { color: #fadb14; font-size: 0.9rem; margin-bottom: 12px; }
  .rating-text { color: #888; font-size: 0.75rem; margin-left: 5px; }

  .card-footer {
    padding: 15px 20px; background: #fffcfc; border-top: 1px solid #eee;
    display: flex; justify-content: space-between; align-items: center;
  }
  .price-tag { color: #ff4d4f; font-weight: 800; font-size: 1rem; }
  .action-btn { color: #ff4d4f; font-weight: bold; font-size: 0.85rem; }
</style>

<div class="hero-banner">
  <h1 style="font-size: 3rem; margin-bottom: 10px;">選品智庫</h1>
  <p style="font-size: 1.1rem; opacity: 0.9;">🚀 2025 全球電商優惠即時導航 · 讓每一分錢都花得聰明</p>
</div>

<h2 style="margin-bottom: 30px; border-left: 6px solid #ff4d4f; padding-left: 15px; font-weight: 800;">🔥 本週必領折扣</h2>

<div class="shop-grid">
  {% for post in site.posts %}
  {% assign img_id = post.id | split: "/" | last %}
  <a href="{{ post.url }}" class="shop-card">
    <div class="card-img" style="background-image: url('/assets/images/{{ img_id }}.png'), url('/assets/images/{{ img_id }}.jpg');"></div>
    
    <div class="card-body">
      <span class="card-tag"># {{ post.tags | first | default: "熱門選品" }}</span>
      <div class="card-title">{{ post.title }}</div>
      
      <div class="rating-box">
        ★ {{ post.rating | default: "4.8" }}
        <span class="rating-text">推薦指數</span>
      </div>
      
      <p style="font-size: 0.85rem; color: #666; line-height: 1.6; height: 3.2em; overflow: hidden;">
        {{ post.summary | truncate: 60 }}
      </p>
    </div>
    
    <div class="card-footer">
      <span class="price-tag">💰 {{ post.price }}</span>
      <span class="action-btn">查看詳情 →</span>
    </div>
  </a>
  {% endfor %}
</div>