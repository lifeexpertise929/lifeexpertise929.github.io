---
layout: default
title: 選品智庫：{{ "now" | date: "%Y年%m月" }}全網優惠速報站
description: "提供 2025 年最新蝦皮免運、必勝客優惠碼、Klook 折扣券。實測有效，幫您精打細算每一分錢。"
---

<style>
  /* --- 全域設計：手機優先 --- */
  :root {
    --primary-red: #ff4d4f;
    --dark-text: #121212;
    --light-gray: #f4f7f9;
  }
  
  body { 
    background-color: var(--light-gray); 
    color: var(--dark-text);
    /* 手機基礎字體 18px 起跳，確保閱讀不吃力 */
    font-size: clamp(18px, 2.5vw, 22px); 
    line-height: 1.6;
    margin: 0;
    font-family: -apple-system, "Noto Sans TC", "Microsoft JhengHei", sans-serif;
  }

  /* --- 頂部 Banner (增加動態感) --- */
  .hero-banner {
    width: 100%;
    min-height: 220px;
    background: linear-gradient(135deg, rgba(255,77,79,0.9), rgba(255,120,117,0.9)), url('/assets/images/banner.jpg');
    background-size: cover;
    background-position: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    text-align: center;
    padding: 40px 20px;
    border-radius: 0 0 40px 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  }
  .hero-banner h1 { font-size: 2.4rem; margin: 0; font-weight: 900; letter-spacing: 1px; }
  .hero-banner p { font-size: 1.2rem; margin-top: 12px; opacity: 0.95; font-weight: 500; }

  /* --- 分類按鈕 (手機超大觸控版) --- */
  .nav-container { 
    display: flex; 
    justify-content: center; 
    gap: 12px; 
    padding: 30px 15px;
    flex-wrap: wrap; 
    max-width: 1200px;
    margin: 0 auto;
  }
  .nav-btn {
    font-size: 1.2rem; /* 超大按鈕字體 */
    padding: 16px 20px; 
    font-weight: 800; 
    border-radius: 16px;
    border: 2px solid transparent;
    background: white; 
    color: #444; 
    cursor: pointer;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
    flex: 1 1 42%; /* 手機上兩兩排版，好點擊 */
    max-width: 200px;
  }
  .nav-btn.active { 
    background: var(--primary-red); 
    color: white; 
    box-shadow: 0 8px 20px rgba(255, 77, 79, 0.4);
    transform: translateY(-3px);
  }

  /* --- 產品網格：電腦 3 欄 / 手機 1 欄 --- */
  .grid-container {
    display: grid;
    /* 電腦版設定為 3 欄 (約 360px 一個) */
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 30px; 
    max-width: 1200px; 
    margin: 0 auto; 
    padding: 0 20px 80px;
  }

  /* --- 產品卡片設計 --- */
  .coupon-card {
    background: white; 
    border-radius: 24px; 
    overflow: hidden;
    display: flex; 
    flex-direction: column; 
    text-decoration: none !important; 
    color: inherit;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border: 1px solid rgba(0,0,0,0.03);
    height: 100%;
  }
  .coupon-card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.1); }

  .image-wrapper {
    width: 100%; padding-top: 56.25%; position: relative; background: #fff;
  }
  .image-wrapper img {
    position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
    max-width: 85%; max-height: 85%; object-fit: contain;
  }

  .content-wrapper { padding: 25px; display: flex; flex-direction: column; flex-grow: 1; }
  .category-tag { color: var(--primary-red); font-size: 1rem; font-weight: 900; margin-bottom: 8px; }
  
  .product-title { 
    font-size: 1.4rem; 
    font-weight: 800; 
    margin-bottom: 12px; 
    line-height: 1.45;
    color: #000;
  }
  .product-summary { 
    font-size: 1.1rem; 
    color: #555; 
    margin-bottom: 25px;
    line-height: 1.6;
  }

  .card-footer { 
    margin-top: auto; padding-top: 20px; border-top: 1px dashed #eee;
    display: flex; justify-content: space-between; align-items: center;
  }
  .price-text { color: var(--primary-red); font-weight: 900; font-size: 1.4rem; }
  .badge-tag { background: #fff2f0; color: var(--primary-red); padding: 4px 12px; border-radius: 8px; font-size: 0.9rem; font-weight: 700; }

  .is-hidden { display: none !important; }

  /* --- 手機版特別微調 --- */
  @media (max-width: 600px) {
    .grid-container { 
      grid-template-columns: 1fr; /* 手機強制一欄，讓字體最大化 */
      padding: 0 15px; 
    }
    .hero-banner h1 { font-size: 1.8rem; }
    .nav-btn { font-size: 1.1rem; padding: 14px 10px; }
    .product-title { font-size: 1.3rem; }
  }
</style>

<div class="hero-banner">
  <h1>選品智庫 💡</h1>
  <p>{{ "now" | date: "%Y 年 %m 月" }} 隱藏優惠與省錢攻略</p>
</div>

<div class="nav-container">
  <button class="nav-btn active" onclick="filterData('all', this)">全部優惠</button>
  <button class="nav-btn" onclick="filterData('美食類', this)">🍕 美食美食</button>
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
          <span class="badge-tag">{{ post.badge | default: "實測有效" }}</span>
        </div>
      </div>
    </a>
  </div>
  {% endfor %}
</div>

<script>
function filterData(category, btn) {
  // 1. 更新按鈕樣式
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  // 2. 過濾卡片內容
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