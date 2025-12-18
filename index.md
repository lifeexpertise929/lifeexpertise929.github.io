---
layout: default
title: 選品智庫 - 全球優惠導航
---

<style>
  /* 1. 頁面加寬與基礎設定 */
  .main-content, .container { max-width: 1100px !important; width: 95% !important; margin: 0 auto; }
  
  /* 2. 頂部 Hero 區 */
  .hero-banner {
    width: 100%; height: 260px;
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('/assets/images/hero-bg.jpg') no-repeat center center;
    background-size: cover; border-radius: 15px;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    color: white; margin-bottom: 40px; text-align: center;
  }
  .hero-banner h1 { font-size: 2.5rem; margin: 0; font-weight: 800; }

  /* 3. 網格佈局 - 確保一行顯示多個卡片 */
  .shop-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 25px; padding-bottom: 50px;
  }

  /* 4. 卡片樣式修復 */
  .shop-card {
    background: #fff; border-radius: 12px; overflow: hidden;
    border: 1px solid #eee; display: flex; flex-direction: column;
    text-decoration: none !important; color: #333 !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  .shop-card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }

  /* 5. 圖片預覽區 */
  .card-img-box {
    width: 100%; height: 160px; background: #f9f9f9;
    background-size: contain; background-repeat: no-repeat; background-position: center;
    border-bottom: 1px solid #f0f0f0;
  }

  /* 6. 文字內容區 */
  .card-body { padding: 15px; flex-grow: 1; }
  .card-tag { color: #ff4d4f; font-size: 0.75rem; font-weight: bold; }
  .card-title { font-size: 1.15rem; font-weight: bold; margin: 8px 0; line-height: 1.4; color: #111; }
  .stars { color: #fadb14; font-size: 0.85rem; margin-bottom: 10px; }
  .card-desc { font-size: 0.85rem; color: #666; line-height: 1.5; }

  /* 7. 底部價格區 */
  .card-footer {
    padding: 12px 15px; background: #fffafa; border-top: 1px solid #fef0f0;
    display: flex; justify-content: space-between; align-items: center;
  }
  .price-text { color: #ff4d4f; font-weight: 800; }
  .btn-link { font-size: 0.8rem; font-weight: bold; color: #ff4d4f; }
</style>

<div class="hero-banner">
  <h1>選品智庫</h1>
  <p>🚀 2025 全球電商優惠即時導航</p>
</div>

<h2 style="margin-bottom: 25px; border-left: 5px solid #ff4d4f; padding-left: 15px;">🔥 本週必領折扣</h2>

<div class="shop-grid">
  {% for post in site.posts %}
  {% assign img_id = post.id | split: "/" | last %}
  <a href="{{ post.url }}" class="shop-card">
    <div class="card-img-box" style="background-image: url('/assets/images/{{ img_id }}.jpg');">
      </div>
    
    <div class="card-body">
      <span class="card-tag"># {{ post.tags | first }}</span>
      <div class="card-title">{{ post.title }}</div>
      
      <div class="stars">★ 4.5 <span style="color:#999; font-size: 0.7rem;">(100+ 評價)</span></div>
      
      <p class="card-desc">{{ post.summary | truncate: 50 }}</p>
    </div>
    
    <div class="card-footer">
      <span class="price-text">💰 {{ post.price }}</span>
      <span class="btn-link">立即領取 →</span>
    </div>
  </a>
  {% endfor %}
</div>