---
layout: default
title: 選品智庫 - 全台最優惠導航
---

<style>
  /* 全域字體與背景優化 */
  :root {
    --main-red: #ff4d4f;
    --text-color: #262626;
    --gray-bg: #f5f7fa;
  }
  
  body { 
    background-color: var(--gray-bg); 
    color: var(--text-color);
    font-size: clamp(14px, 1vw + 10px, 18px); /* 字體隨螢幕縮放 */
    line-height: 1.6;
  }

  /* 旗艦級 Hero Banner (高度隨螢幕調整) */
  .hero-banner {
    width: 100%;
    min-height: 250px;
    height: 35vh; /* 佔據螢幕高度的 35% */
    background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('/assets/images/banner.jpg');
    background-size: cover;
    background-position: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    text-align: center;
    padding: 20px;
    margin-bottom: 2rem;
  }
  .hero-banner h1 { font-size: clamp(2rem, 5vw, 3.5rem); margin: 0; font-weight: 800; }
  .hero-banner p { font-size: clamp(0.9rem, 2vw, 1.2rem); opacity: 0.9; }

  /* 分類導航 (手機自動換行) */
  .nav-container { 
    display: flex; 
    justify-content: center; 
    gap: 10px; 
    padding: 0 15px;
    margin-bottom: 2rem; 
    flex-wrap: wrap; 
  }
  .nav-btn {
    padding: 10px 20px; 
    border-radius: 50px; 
    border: 2px solid #fff;
    background: white; 
    color: #555; 
    font-weight: 600; 
    cursor: pointer;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
    transition: 0.3s;
    font-size: 0.95rem;
  }
  .nav-btn.active { background: var(--main-red); color: white; border-color: var(--main-red); }

  /* 響應式產品網格 */
  .grid-container {
    display: grid;
    /* 關鍵：使用 auto-fit 讓卡片自動填滿，最窄 280px */
    grid-template-columns: repeat(auto-fill, minmax(min(100%, 300px), 1fr));
    gap: 25px; 
    max-width: 1240px; 
    margin: 0 auto; 
    padding: 0 20px 50px;
  }

  /* 卡片設計 */
  .coupon-card {
    background: white; 
    border-radius: 16px; 
    overflow: hidden;
    display: flex; 
    flex-direction: column; 
    text-decoration: none !important; 
    color: inherit;
    transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    border: 1px solid #eee;
  }
  .coupon-card:hover { transform: translateY(-8px); box-shadow: 0 12px 24px rgba(0,0,0,0.1); }

  /* 圖片比例容器 (16:9) */
  .image-wrapper {
    position: relative;
    width: 100%;
    padding-top: 56.25%; /* 16:9 比例 */
    background: #fff;
    border-bottom: 1px solid #f0f0f0;
  }
  .image-wrapper img {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    max-width: 85%; max-height: 85%;
    object-fit: contain;
  }

  /* 內容區塊 */
  .content-wrapper { padding: 20px; display: flex; flex-direction: column; flex-grow: 1; }
  .category-tag { color: var(--main-red); font-size: 0.8rem; font-weight: bold; margin-bottom: 5px; }
  .product-title { 
    font-size: 1.15rem; 
    font-weight: 700; 
    margin-bottom: 10px; 
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
    height: 2.8em; line-height: 1.4;
  }
  .product-summary { 
    font-size: 0.95rem; 
    color: #666; 
    margin-bottom: 20px;
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
    height: 3em;
  }

  .card-footer { 
    margin-top: auto; padding-top: 15px; border-top: 1px dashed #eee;
    display: flex; justify-content: space-between; align-items: center;
  }
  .price-text { color: var(--main-red); font-weight: 800; font-size: 1.1rem; }
  .review-text { font-size: 0.85rem; color: #999; }

  .is-hidden { display: none !important; }

  /* 手機版微調 */
  @media (max-width: 600px) {
    .grid-container { padding: 0 15px; gap: 20px; }
    .hero-banner { min-height: 200px; border-radius: 0 0 25px 25px; }
  }
</style>

<div class="hero-banner">
  <h1>選品智庫 💡</h1>
  <p>掌握即時優惠，省錢更有品味</p>
</div>

<div class="nav-container">
  <button class="nav-btn active" onclick="filterData('all', this)">全部</button>
  <button class="nav-btn" onclick="filterData('美食類', this)">🍕 美食</button>
  <button class="nav-btn" onclick="filterData('旅遊類', this)">✈️ 旅遊</button>
  <button class="nav-btn" onclick="filterData('購物網站', this)">🛒 購物</button>
</div>

<div class="grid-container" id="couponGrid">
  {% for post in site.posts %}
  {% assign cat = post.tags | first %}
  <div class="item-box" data-cat="{{ cat }}">
    <a href="{{ post.url }}" class="coupon-card">
      <div class="image-wrapper">
        <img src="/assets/images/{{ post.filename | replace: '.md', '' }}.jpg" 
             onerror="this.src='/assets/images/{{ post.filename | replace: '.md', '' }}.png'">
      </div>
      <div class="content-wrapper">
        <div class="category-tag">{{ cat }}</div>
        <div class="product-title">{{ post.title }}</div>
        <div class="product-summary">{{ post.summary }}</div>
        <div class="card-footer">
          <span class="price-text">{{ post.price }}</span>
          <span class="review-text">★ {{ post.rating }} ({{ post.reviews }})</span>
        </div>
      </div>
    </a>
  </div>
  {% endfor %}
</div>

<script>
function filterData(category, btn) {
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  document.querySelectorAll('.item-box').forEach(item => {
    const itemCat = item.getAttribute('data-cat');
    if (category === 'all' || itemCat === category) {
      item.classList.remove('is-hidden');
    } else {
      item.classList.add('is-hidden');
    }
  });
}
</script>