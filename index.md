---
layout: default
title: 選品智庫 - 全球優惠導航
---

<style>
  /* 1. 全域容器加寬 */
  .main-content, .container { 
    max-width: 1200px !important; 
    width: 95% !important; 
    margin: 0 auto; 
  }

  /* 2. 頂部 Hero Banner */
  .hero-banner {
    width: 100%;
    height: 280px;
    background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('/assets/images/hero-bg.jpg') no-repeat center center;
    background-size: cover;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
    margin-bottom: 40px;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
  }
  .hero-banner h1 { font-size: 2.8rem; font-weight: 800; margin: 0; }
  .hero-banner p { font-size: 1.1rem; margin-top: 10px; opacity: 0.95; }

  /* 3. 修復網格佈局：確保卡片三欄排列 */
  .shop-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 30px;
    padding-bottom: 60px;
  }

  /* 4. 卡片精緻設計 */
  .shop-card {
    background: #ffffff;
    border-radius: 16px;
    border: 1px solid #f0f0f0;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    text-decoration: none !important;
    transition: all 0.3s ease;
  }
  .shop-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.08);
    border-color: #ff4d4f;
  }

  /* 5. 圖片預覽區：解決 PNG/JPG 混合問題 */
  .card-img-wrapper {
    width: 100%;
    height: 180px;
    background-color: #f9f9f9;
    background-position: center;
    background-repeat: no-repeat;
    background-size: contain;
    border-bottom: 1px solid #f5f5f5;
  }

  .card-content { padding: 20px; flex-grow: 1; }
  .card-category { color: #ff4d4f; font-size: 0.75rem; font-weight: 700; margin-bottom: 8px; display: block; }
  .card-title { font-size: 1.2rem; font-weight: 800; color: #1a1a1a; line-height: 1.4; margin-bottom: 10px; }
  
  /* 星等區域 */
  .card-rating { color: #fadb14; font-size: 0.9rem; margin-bottom: 12px; }
  .card-rating span { color: #999; font-size: 0.75rem; margin-left: 5px; }

  .card-summary { font-size: 0.85rem; color: #666; line-height: 1.6; height: 3.2em; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; }

  /* 6. 卡片底部按鈕 */
  .card-footer {
    padding: 15px 20px;
    background: #fffcfc;
    border-top: 1px solid #fff0f0;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .price-highlight { color: #ff4d4f; font-weight: 800; }
  .btn-text { color: #ff4d4f; font-weight: 700; font-size: 0.85rem; }
</style>

<div class="hero-banner">
  <h1>選品智庫</h1>
  <p>🚀 2025 全球電商優惠即時導航</p>
</div>

<h2 style="margin-bottom: 30px; border-left: 5px solid #ff4d4f; padding-left: 15px; font-weight: 800;">🔥 本週必領折扣</h2>

<div class="shop-grid">
  {% for post in site.posts %}
  {% assign img_id = post.id | split: "/" | last %}
  <a href="{{ post.url }}" class="shop-card">
    <div class="card-img-wrapper" style="background-image: url('/assets/images/{{ img_id }}.png'), url('/assets/images/{{ img_id }}.jpg');">
    </div>
    
    <div class="card-content">
      <span class="card-category"># {{ post.tags | first }}</span>
      <div class="card-title">{{ post.title }}</div>
      
      <div class="card-rating">
        ★ {{ post.rating | default: "4.5" }} <span>(100+ 評價)</span>
      </div>
      
      <p class="card-summary">{{ post.summary }}</p>
    </div>
    
    <div class="card-footer">
      <span class="price-highlight">💰 {{ post.price }}</span>
      <span class="btn-text">立即領取 →</span>
    </div>
  </a>
  {% endfor %}
</div>