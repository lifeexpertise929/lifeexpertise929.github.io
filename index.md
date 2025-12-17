---
layout: default
title: 選品智庫 - AI 驅動的極致省錢術
---

<style>
  /* 讓版面變寬，在大螢幕顯示三欄，減少拉動長度 */
  .main-content, .container { 
    max-width: 1200px !important; 
    width: 95% !important; 
    margin: 0 auto;
  }

  /* 頂部 Hero 區域：指向正確的 assets/images 路徑 */
  .hero-section {
    position: relative;
    width: 100%;
    height: 350px;
    background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('/assets/images/hero-bg.jpg') no-repeat center center;
    background-size: cover;
    border-radius: 20px;
    margin-bottom: 45px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    text-align: center;
  }

  .hero-title { font-size: 3.2rem; font-weight: 900; margin: 0; text-shadow: 0 4px 15px rgba(0,0,0,0.6); }
  .hero-subtitle { font-size: 1.2rem; opacity: 0.9; margin-top: 15px; }

  /* 網格佈局 */
  .post-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 30px;
    padding-bottom: 60px;
  }

  /* 卡片設計 */
  .post-card {
    background: #ffffff;
    border: 1px solid #f0f0f0;
    border-radius: 16px;
    overflow: hidden;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    text-decoration: none !important;
    color: #333 !important;
  }

  .post-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 25px 50px rgba(0,0,0,0.1);
    border-color: #ff4d4f;
  }

  /* 圖片預覽區 */
  .card-preview {
    width: 100%;
    height: 180px;
    background: #fafafa;
    border-bottom: 1px solid #f0f0f0;
    display: flex;
    align-items: center;
    justify-content: center;
    background-size: contain; /* 改為 contain 確保 Logo 不會被裁切 */
    background-repeat: no-repeat;
    background-position: center;
  }

  .card-content { padding: 20px; flex-grow: 1; }
  .card-tag { font-size: 0.75rem; color: #ff4d4f; font-weight: 700; margin-bottom: 10px; display: block; }
  .card-title { font-size: 1.25rem; font-weight: 800; margin-bottom: 12px; line-height: 1.4; color: #111; }
  .card-summary { font-size: 0.9rem; color: #666; line-height: 1.6; height: 3.2em; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; }

  .card-footer {
    padding: 15px 20px;
    background: #fffcfc;
    border-top: 1px solid #fef0f0;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .card-price { color: #ff4d4f; font-weight: bold; font-size: 0.95rem; }
  .card-more { color: #ff4d4f; font-size: 0.85rem; font-weight: bold; }
</style>

<div class="hero-section">
  <h1 class="hero-title">選品智庫</h1>
  <p class="hero-subtitle">🚀 2025 全球電商優惠即時導航 • 讓每一分錢都花得聰明</p>
</div>

<h2 style="margin-bottom: 30px; font-weight: 800; border-left: 5px solid #ff4d4f; padding-left: 15px;">🔥 本週必領折扣</h2>

<div class="post-grid">
  {% for post in site.posts %}
  <a href="{{ post.url }}" class="post-card">
    {% assign img_name = post.id | split: "/" | last %}
    <div class="card-preview" style="background-image: url('/assets/images/{{ img_name }}.jpg');">
      {% if post.title contains 'YAHOO' %}
      <div class="card-preview" style="background-image: url('/assets/images/{{ img_name }}.png'); border-bottom:none;"></div>
      {% endif %}
      
      <div id="fallback-text" style="display:none;">{{ post.title | truncate: 10 }}</div>
    </div>
    
    <div class="card-content">
      <span class="card-tag"># {{ post.tags | first }}</span>
      <div class="card-title">{{ post.title }}</div>
      <p class="card-summary">{{ post.summary }}</p>
    </div>
    
    <div class="card-footer">
      <span class="card-price">💰 {{ post.price }}</span>
      <span class="card-more">立即領取 →</span>
    </div>
  </a>
  {% endfor %}
</div>