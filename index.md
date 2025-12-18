---
layout: default
title: 選品智庫 - 專業導購領航
---

<style>
  /* 1. 全域版面加寬，在大螢幕呈現三欄佈局 */
  .main-content, .container { 
    max-width: 1200px !important; 
    width: 95% !important; 
    margin: 0 auto; 
  }

  /* 2. 頂部大圖區 (Hero Section) */
  .hero-banner {
    width: 100%;
    height: 300px;
    background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('/assets/images/hero-bg.jpg') no-repeat center center;
    background-size: cover;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
    margin-bottom: 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    text-align: center;
  }
  .hero-banner h1 { font-size: 3rem; font-weight: 900; margin: 0; text-shadow: 0 4px 10px rgba(0,0,0,0.5); }
  .hero-banner p { font-size: 1.2rem; margin-top: 10px; opacity: 0.9; }

  /* 3. 網格容器 */
  .shop-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 30px;
    padding-bottom: 60px;
  }

  /* 4. 卡片設計 - 模仿專業電商質感 */
  .shop-card {
    background: #fff;
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid #f0f0f0;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    text-decoration: none !important;
    color: #333 !important;
  }
  .shop-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    border-color: #ff4d4f;
  }

  /* 5. 圖片顯示區 - 解決 JPG/PNG 混合問題 */
  .card-image {
    width: 100%;
    height: 180px;
    background-color: #fcfcfc;
    background-position: center;
    background-repeat: no-repeat;
    background-size: contain; /* 確保 Logo 完整不被裁切 */
    border-bottom: 1px solid #f5f5f5;
  }

  .card-content { padding: 20px; flex-grow: 1; }
  .card-tag { color: #ff4d4f; font-size: 0.75rem; font-weight: bold; margin-bottom: 8px; display: block; }
  .card-title { font-size: 1.2rem; font-weight: bold; color: #111; margin-bottom: 10px; line-height: 1.4; }
  
  /* 動態星等樣式 */
  .stars { color: #fadb14; font-size: 0.9rem; margin-bottom: 12px; }
  .stars span { color: #999; font-size: 0.75rem; margin-left: 5px; }

  .card-summary { 
    font-size: 0.85rem; 
    color: #666; 
    line-height: 1.6; 
    height: 3.2em; 
    overflow: hidden; 
    display: -webkit-box; 
    -webkit-line-clamp: 2; 
    -webkit-box-orient: vertical; 
  }

  /* 6. 卡片底部 */
  .card-footer {
    padding: 15px 20px;
    background: #fffafa;
    border-top: 1px solid #fdf0f0;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .price-tag { color: #ff4d4f; font-weight: 800; font-size: 1rem; }
  .btn-action { color: #ff4d4f; font-weight: bold; font-size: 0.85rem; }
</style>

<div class="hero-banner">
  <h1>選品智庫</h1>
  <p>🚀 2025 全球電商優惠即時導航</p>
</div>

<h2 style="margin-bottom: 30px; border-left: 5px solid #ff4d4f; padding-left: 15px; font-weight: 800;">🔥 本週必領折扣</h2>

<div class="shop-grid">
  {% for post in site.posts %}
  {% assign img_name = post.id | split: "/" | last %}
  <a href="{{ post.url }}" class="shop-card">
    
    <div class="card-image" style="background-image: url('/assets/images/{{ img_name }}.png'), url('/assets/images/{{ img_name }}.jpg');">
    </div>
    
    <div class="card-content">
      <span class="card-tag"># {{ post.tags | first }}</span>
      <div class="card-title">{{ post.title }}</div>
      
      <div class="stars">
        ★ {{ post.rating | default: "4.5" }} <span>(100+ 評價)</span>
      </div>
      
      <p class="card-summary">{{ post.summary }}</p>
    </div>
    
    <div class="card-footer">
      <span class="price-tag">💰 {{ post.price }}</span>
      <span class="btn-action">立即領取 →</span>
    </div>
  </a>
  {% endfor %}
</div>