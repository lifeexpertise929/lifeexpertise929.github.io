---
layout: default
title: 選品智庫 - 全台最優惠導航
---

<style>
  /* --- 全域設定 --- */
  :root {
    --primary-red: #ff4d4f;
    --dark-text: #262626;
    --light-gray: #f8fafc;
  }
  
  body { 
    background-color: var(--light-gray); 
    color: var(--dark-text);
    font-size: clamp(16px, 1vw + 12px, 20px); /* 流體字體大小 */
    line-height: 1.6;
    margin: 0;
  }

  /* --- 旗艦級 Hero Banner --- */
  .hero-banner {
    width: 100%;
    min-height: 280px;
    height: 35vh;
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('/assets/images/banner.jpg');
    background-size: cover;
    background-position: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    text-align: center;
    padding: 20px;
    border-radius: 0 0 30px 30px;
    margin-bottom: 2rem;
  }
  .hero-banner h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0; font-weight: 800; letter-spacing: 2px; }
  .hero-banner p { font-size: clamp(1rem, 2.5vw, 1.3rem); opacity: 0.9; margin-top: 10px; }

  /* --- 分類按鈕區 (放大版) --- */
  .nav-container { 
    display: flex; 
    justify-content: center; 
    gap: 15px; 
    padding: 20px 15px;
    margin-bottom: 2.5rem; 
    flex-wrap: wrap; 
  }
  .nav-btn {
    font-size: 1.25rem;      /* 顯著放大字體 */
    padding: 15px 35px;     /* 增加點擊面積 */
    font-weight: 700; 
    border-radius: 50px; 
    border: none;
    background: white; 
    color: #444; 
    cursor: pointer;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1); 
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  }
  .nav-btn.active { 
    background: var(--primary-red); 
    color: white; 
    transform: translateY(-5px); 
    box-shadow: 0 10px 25px rgba(255, 77, 79, 0.4);
  }

  /* --- 產品網格 (電腦 3 欄) --- */
  .grid-container {
    display: grid;
    /* 設定最小寬度，讓電腦端自動維持在 3 欄左右 */
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 35px; 
    max-width: 1200px; 
    margin: 0 auto; 
    padding: 0 25px 60px;
  }

  /* --- 卡片設計 --- */
  .coupon-card {
    background: white; 
    border-radius: 20px; 
    overflow: hidden;
    display: flex; 
    flex-direction: column; 
    text-decoration: none !important; 
    color: inherit;
    transition: all 0.4s ease;
    border: 1px solid rgba(0,0,0,0.05);
    height: 100%;
  }
  .coupon-card:hover { transform: translateY(-12px); box-shadow: 0 20px 40px rgba(0,0,0,0.12); }

  /* 圖片比例容器 (16:9) */
  .image-wrapper {
    position: relative;
    width: 100%;
    padding-top: 56.25%; 
    background: #fff;
    border-bottom: 1px solid #f1f1f1;
  }
  .image-wrapper img {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    max-width: 80%; max-height: 80%;
    object-fit: contain;
  }

  /* 內容區塊 */
  .content-wrapper { padding: 25px; display: flex; flex-direction: column; flex-grow: 1; }
  .category-tag { color: var(--primary-red); font-size: 0.9rem; font-weight: 800; margin-bottom: 8px; text-transform: uppercase; }
  .product-title { 
    font-size: 1.3rem; 
    font-weight: 800; 
    margin-bottom: 12px; 
    height: 2.8em; line-height: 1.4;
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
  }
  .product-summary { 
    font-size: 1rem; 
    color: #666; 
    margin-bottom: 25px;
    height: 3em;
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
  }

  /* 底部數值區 */
  .card-footer { 
    margin-top: auto; padding-top: 20px; border-top: 1px dashed #eee;
    display: flex; justify-content: space-between; align-items: center;
  }
  .price-text { color: var(--primary-red); font-weight: 900; font-size: 1.2rem; }
  .review-text { font-size: 0.9rem; color: #aaa; font-weight: 500; }

  .is-hidden { display: none !important; }

  /* --- 響應式微調 --- */
  @media (max-width: 800px) {
    .grid-container { grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); }
  }
  @media (max-width: 600px) {
    .nav-btn { font-size: 1.1rem; padding: 12px 20px; flex: 1 1 42%; }
    .grid-container { grid-template-columns: 1fr; padding: 0 15px; }
  }
</style>

<div class="hero-banner">
  <h1>選品智庫 💡</h1>
  <p>最完整的購物、美食、旅遊優惠導航</p>
</div>

<div class="nav-container">
  <button class="nav-btn active" onclick="filterData('all', this)">全部項目</button>
  <button class="nav-btn" onclick="filterData('美食類', this)">🍕 美食優惠</button>
  <button class="nav-btn" onclick="filterData('旅遊類', this)">✈️ 旅遊行程</button>
  <button class="nav-btn" onclick="filterData('購物網站', this)">🛒 購物省錢</button>
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
        <div class="category-tag"># {{ cat }}</div>
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
  // 1. 切換按鈕狀態
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  // 2. 執行卡片過濾
  const items = document.querySelectorAll('.item-box');
  items.forEach(item => {
    const itemCat = item.getAttribute('data-cat');
    if (category === 'all' || itemCat === category) {
      item.classList.remove('is-hidden');
    } else {
      item.classList.add('is-hidden');
    }
  });
}
</script>