---
layout: default
title: 選品智庫 - 全台最優惠導航
---

<style>
  /* --- 全域設定：針對手機字體強化 --- */
  :root {
    --primary-red: #ff4d4f;
    --dark-text: #1a1a1a; /* 加深顏色，對比度更高更好讀 */
    --light-gray: #f8fafc;
  }
  
  body { 
    background-color: var(--light-gray); 
    color: var(--dark-text);
    /* 手機上至少 18px，電腦上可達 22px */
    font-size: clamp(18px, 2vw + 12px, 22px); 
    line-height: 1.7; /* 增加行距，閱讀更輕鬆 */
    margin: 0;
    font-family: -apple-system, "Noto Sans TC", "Microsoft JhengHei", sans-serif;
  }

  /* --- 旗艦級 Hero Banner --- */
  .hero-banner {
    width: 100%;
    min-height: 250px;
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('/assets/images/banner.jpg');
    background-size: cover;
    background-position: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    text-align: center;
    padding: 30px 20px;
    border-radius: 0 0 30px 30px;
  }
  .hero-banner h1 { font-size: 2.5rem; margin: 0; font-weight: 900; }
  .hero-banner p { font-size: 1.2rem; margin-top: 10px; opacity: 0.9; }

  /* --- 分類按鈕區 (手機版超大按鈕) --- */
  .nav-container { 
    display: flex; 
    justify-content: center; 
    gap: 12px; 
    padding: 25px 15px;
    flex-wrap: wrap; 
  }
  .nav-btn {
    /* 這裡再次加大字體 */
    font-size: 1.2rem; 
    padding: 15px 25px; 
    font-weight: 800; 
    border-radius: 12px; /* 方圓形更有質感 */
    border: none;
    background: white; 
    color: #333; 
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    flex: 1 1 42%; /* 手機上兩兩一排，佔滿寬度 */
    max-width: 200px;
  }
  .nav-btn.active { 
    background: var(--primary-red); 
    color: white; 
    box-shadow: 0 6px 15px rgba(255, 77, 79, 0.4);
  }

  /* --- 產品網格 (電腦 3 欄 / 手機 1 欄) --- */
  .grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 30px; 
    max-width: 1200px; 
    margin: 0 auto; 
    padding: 0 20px 60px;
  }

  /* --- 卡片文字強化 --- */
  .coupon-card {
    background: white; 
    border-radius: 20px; 
    overflow: hidden;
    display: flex; 
    flex-direction: column; 
    text-decoration: none !important; 
    color: inherit;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    height: 100%;
  }

  .image-wrapper {
    width: 100%; padding-top: 56%; position: relative; background: #fff;
  }
  .image-wrapper img {
    position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
    max-width: 80%; max-height: 80%; object-fit: contain;
  }

  .content-wrapper { padding: 25px; }
  .category-tag { color: var(--primary-red); font-size: 1rem; font-weight: 900; margin-bottom: 10px; }
  
  /* 標題字體加大 */
  .product-title { 
    font-size: 1.4rem; 
    font-weight: 800; 
    margin-bottom: 12px; 
    line-height: 1.4;
    color: #000;
  }
  /* 摘要字體加大 */
  .product-summary { 
    font-size: 1.1rem; 
    color: #555; 
    margin-bottom: 20px;
  }

  .card-footer { 
    margin-top: auto; padding-top: 20px; border-top: 1px dashed #eee;
    display: flex; justify-content: space-between; align-items: center;
  }
  .price-text { color: var(--primary-red); font-weight: 900; font-size: 1.3rem; }
  .review-text { font-size: 1rem; color: #888; }

  .is-hidden { display: none !important; }

  /* --- 手機版特別強化 --- */
  @media (max-width: 600px) {
    body { font-size: 18px; }
    .product-title { font-size: 1.3rem; }
    .product-summary { font-size: 1.1rem; }
    .nav-btn { font-size: 1.1rem; padding: 12px 10px; }
    .grid-container { grid-template-columns: 1fr; } /* 強制手機一列一個，字才夠寬 */
  }
</style>

<div class="hero-banner">
  <h1>選品智庫 💡</h1>
  <p>最完整的購物、美食、旅遊優惠導航</p>
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
        <div class="category-tag"># {{ cat }}</div>
        <div class="product-title">{{ post.title }}</div>
        <div class="product-summary">{{ post.summary }}</div>
        <div class="card-footer">
          <span class="price-text">{{ post.price }}</span>
          <span class="review-text">★ {{ post.rating }}</span>
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