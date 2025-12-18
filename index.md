---
layout: default
title: 選品智庫 - 專業導購領航
---

<style>
  /* 全域容器與專業網格設定 */
  .main-content, .container { 
    max-width: 1200px !important; 
    width: 95% !important; 
    margin: 0 auto; 
  }

  .shop-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 30px;
    padding: 20px 0 60px;
  }

  /* 模仿專業電商卡片 */
  .shop-card {
    background: #fff;
    border-radius: 16px;
    border: 1px solid #eee;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    text-decoration: none !important;
    transition: all 0.3s ease;
  }
  .shop-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.1);
  }

  /* 圖片顯示邏輯：自動適應 PNG/JPG */
  .card-img {
    width: 100%;
    height: 180px;
    background-color: #fcfcfc;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    border-bottom: 1px solid #f5f5f5;
  }

  .card-body { padding: 20px; flex-grow: 1; }
  .card-title { font-size: 1.15rem; font-weight: 800; color: #1a1a1a; margin-bottom: 8px; }
  
  /* 動態星等顏色 */
  .stars { color: #fadb14; font-size: 0.9rem; margin-bottom: 10px; }
  
  .card-footer {
    padding: 15px 20px;
    background: #fffcfc;
    border-top: 1px solid #eee;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .price { color: #ff4d4f; font-weight: bold; }
</style>

<div style="width:100%; height:260px; background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('/assets/images/hero-bg.jpg') center/cover; border-radius: 20px; display: flex; flex-direction: column; align-items: center; justify-content: center; color: white; text-align: center; margin-bottom: 40px;">
  <h1 style="font-size: 2.8rem; margin: 0;">選品智庫</h1>
  <p>🚀 2025 全球電商優惠即時導航</p>
</div>

<h2 style="border-left: 5px solid #ff4d4f; padding-left: 15px; margin-bottom: 30px;">🔥 本週必領折扣</h2>

<div class="shop-grid">
  {% for post in site.posts %}
  {% assign img_id = post.id | split: "/" | last %}
  <a href="{{ post.url }}" class="shop-card">
    <div class="card-img" style="background-image: url('/assets/images/{{ img_id }}.png'), url('/assets/images/{{ img_id }}.jpg');"></div>
    
    <div class="card-body">
      <span style="color:#ff4d4f; font-size:0.75rem; font-weight:bold;"># {{ post.tags | first }}</span>
      <div class="card-title">{{ post.title }}</div>
      
      <div class="stars">★ {{ post.rating | default: "4.5" }} <span style="color:#999; font-size:0.75rem;">(100+ 評價)</span></div>
      
      <p style="font-size: 0.85rem; color: #666; line-height: 1.5;">{{ post.summary }}</p>
    </div>
    
    <div class="card-footer">
      <span class="price">💰 {{ post.price }}</span>
      <span style="color:#ff4d4f; font-weight:bold; font-size:0.85rem;">查看詳情 →</span>
    </div>
  </a>
  {% endfor %}
</div>