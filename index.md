---
layout: default
title: 選品智庫 - AI 驅動的極致省錢術
---

<style>
  /* 1. 頂部大圖 Hero Section */
  .hero-section {
    position: relative;
    width: 100%;
    height: 300px; /* 您可以調整高度 */
    background: url('hero-bg.jpg') no-repeat center center;
    background-size: cover;
    border-radius: 15px;
    margin-bottom: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    text-shadow: 0 2px 10px rgba(0,0,0,0.5);
  }

  .hero-overlay {
    text-align: center;
    background: rgba(0, 0, 0, 0.2); /* 讓文字在圖片上更清楚 */
    padding: 20px;
    border-radius: 10px;
  }

  .hero-title { font-size: 2.5rem; font-weight: bold; margin: 0; }
  .hero-subtitle { font-size: 1.1rem; opacity: 0.9; }

  /* 2. 文章網格佈局 */
  .post-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 25px;
  }

  /* 3. 卡片設計 - 模仿專業選品站 */
  .post-card {
    background: #fff;
    border: 1px solid #eee;
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    text-decoration: none !important;
    color: #333 !important;
  }

  .post-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    border-color: #d32f2f;
  }

  /* 這裡預設放一張分類縮圖，若以後有產品圖可更換 */
  .post-image-placeholder {
    width: 100%;
    height: 160px;
    background: #f8f9fa;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    border-bottom: 1px solid #eee;
  }

  .post-content { padding: 20px; flex-grow: 1; }
  
  .post-tag {
    font-size: 0.75rem;
    color: #d32f2f;
    text-transform: uppercase;
    font-weight: bold;
    margin-bottom: 8px;
  }

  .post-card-title {
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 10px;
    line-height: 1.4;
  }

  .post-card-summary {
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 15px;
    line-height: 1.5;
  }

  .post-footer {
    padding: 15px 20px;
    background: #fafafa;
    border-top: 1px solid #eee;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .price-tag { color: #f57c00; font-weight: bold; font-size: 0.9rem; }
  .btn-go { font-size: 0.8rem; color: #d32f2f; font-weight: bold; }
</style>

<div class="hero-section">
  <div class="hero-overlay">
    <h1 class="hero-title">選品智庫</h1>
    <p class="hero-subtitle">⚡ AI 驅動的極致省錢術，為您過濾全球優質折扣</p>
  </div>
</div>

<h2 style="margin-bottom: 30px;">🚀 最新優惠速遞</h2>

<div class="post-grid">
  {% for post in site.posts %}
  <a href="{{ post.url }}" class="post-card">
    <div class="post-image-placeholder">
      {% if post.tags contains '居家選品' %} 🏠 {% else %} 🛍️ {% endif %}
    </div>
    <div class="post-content">
      <div class="post-tag">{{ post.tags | first }}</div>
      <div class="post-card-title">{{ post.title }}</div>
      <p class="post-card-summary">{{ post.summary }}</p>
    </div>
    <div class="post-footer">
      <span class="price-tag">💰 {{ post.price }}</span>
      <span class="btn-go">查看詳情 →</span>
    </div>
  </a>
  {% endfor %}
</div>