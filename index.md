---
layout: default
title: 選品智庫 - 全球優惠即時導航
---

<style>
  /* 1. 突破容器限制，讓畫面變寬 */
  .main-content, .container { 
    max-width: 1200px !important; 
    width: 95% !important; 
    margin: 0 auto;
  }

  /* 2. 頂部大圖：增加層次感 */
  .hero-banner {
    width: 100%;
    height: 350px;
    background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('hero-bg.jpg') no-repeat center center;
    background-size: cover;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
    margin-bottom: 50px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
  }

  /* 3. 三欄位網格：資訊更豐富 */
  .shop-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 30px;
  }

  /* 4. 模擬連結預覽卡片 */
  .shop-card {
    background: #fff;
    border-radius: 15px;
    overflow: hidden;
    border: 1px solid #f0f0f0;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    display: flex;
    flex-direction: column;
    text-decoration: none !important;
  }

  .shop-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    border-color: #ff4d4f;
  }

  /* 模擬網站預覽圖區域 */
  .web-preview {
    width: 100%;
    height: 180px;
    background: #f9f9f9;
    position: relative;
    border-bottom: 2px solid #f0f0f0;
    overflow: hidden;
  }

  /* 模擬瀏覽器網址列 */
  .web-browser-bar {
    height: 25px;
    background: #eee;
    display: flex;
    align-items: center;
    padding: 0 10px;
    gap: 5px;
  }
  .dot { width: 6px; height: 6px; border-radius: 50%; background: #bbb; }

  .preview-logo {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 155px;
    font-size: 1.2rem;
    font-weight: bold;
    color: #999;
    background: white;
  }

  .shop-info { padding: 20px; flex-grow: 1; }
  .shop-tag { color: #ff4d4f; font-size: 0.8rem; font-weight: bold; margin-bottom: 10px; display: block; }
  .shop-title { font-size: 1.25rem; font-weight: bold; color: #222; margin-bottom: 12px; }
  .shop-desc { font-size: 0.9rem; color: #666; line-height: 1.6; height: 3em; overflow: hidden; }

  .shop-footer {
    padding: 15px 20px;
    background: #fffafa;
    border-top: 1px solid #fdeeee;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .shop-price { color: #ff4d4f; font-weight: 800; font-size: 1rem; }
  .shop-btn { background: #ff4d4f; color: white !important; padding: 6px 15px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; }
</style>

<div class="hero-banner">
  <h1 style="font-size: 3rem; margin-bottom: 10px;">選品智庫</h1>
  <p style="font-size: 1.2rem; letter-spacing: 2px;">⚡ AI 驅動的極致省錢術，為您過濾全球優質折扣</p>
</div>

<div class="shop-grid">
  {% for post in site.posts %}
  <a href="{{ post.url }}" class="shop-card">
    <div class="web-preview">
      <div class="web-browser-bar">
        <div class="dot"></div><div class="dot"></div><div class="dot"></div>
        <span style="font-size: 10px; color: #aaa; margin-left: 5px;">https://{{ post.title | truncate: 20 }}...</span>
      </div>
      <div class="preview-logo">
        {% if post.title contains 'Yahoo' %} 🟣 Yahoo! {% elsif post.title contains 'Klook' %} 🟠 Klook {% elsif post.title contains '蝦皮' %} 🔴 Shopee {% else %} 🛍️ Official Site {% endif %}
      </div>
    </div>
    <div class="shop-info">
      <span class="shop-tag">{{ post.tags | first }}</span>
      <div class="shop-title">{{ post.title }}</div>
      <p class="shop-desc">{{ post.summary }}</p>
    </div>
    <div class="shop-footer">
      <span class="shop-price">💰 {{ post.price }}</span>
      <span class="shop-btn">前往網站</span>
    </div>
  </a>
  {% endfor %}
</div>