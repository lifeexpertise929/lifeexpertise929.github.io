---
layout: default
title: 選品智庫 - 全台最優惠導航
---

<style>
  /* 全域背景優化 */
  body { background-color: #f4f7f6; color: #333; font-family: "PingFang TC", "Microsoft JhengHei", sans-serif; }

  /* 旗艦級 Hero Banner */
  .hero-banner {
    position: relative;
    width: 100%;
    height: 300px;
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('/assets/images/banner.jpg'); /* 請確保有這張圖或換成現有圖片 */
    background-size: cover;
    background-position: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    text-align: center;
    border-radius: 0 0 40px 40px;
    margin-bottom: 40px;
  }

  /* 分類按鈕精緻化 */
  .nav-container { display: flex; justify-content: center; gap: 15px; margin-bottom: 40px; flex-wrap: wrap; }
  .nav-btn {
    padding: 12px 28px; border-radius: 30px; border: none;
    background: white; color: #666; font-weight: 600; cursor: pointer;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: all 0.3s;
  }
  .nav-btn.active { background: #ff4d4f; color: white; transform: scale(1.05); }

  /* 產品網格佈局 */
  .grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 30px; max-width: 1200px; margin: 0 auto; padding: 0 20px;
  }

  /* 卡片精緻設計 */
  .coupon-card {
    background: white; border-radius: 20px; overflow: hidden;
    box-shadow: 0 10px 20px rgba(0,0,0,0.05); transition: 0.3s;
    display: flex; flex-direction: column; text-decoration: none !important; color: inherit;
  }
  .coupon-card:hover { transform: translateY(-10px); box-shadow: 0 15px 30px rgba(0,0,0,0.1); }

  /* 圖片容器：解決 Logo 被切掉的問題 */
  .image-wrapper {
    width: 100%; height: 180px; background: #fff;
    display: flex; align-items: center; justify-content: center; padding: 20px;
    border-bottom: 1px solid #f0f0f0;
  }
  .image-wrapper img { max-width: 100%; max-height: 100%; object-fit: contain; }

  /* 文字內容區 */
  .content-wrapper { padding: 20px; display: flex; flex-direction: column; flex-grow: 1; }
  .category-tag { color: #ff4d4f; font-size: 0.85rem; font-weight: bold; margin-bottom: 8px; }
  .product-title { font-size: 1.1rem; font-weight: 700; margin-bottom: 10px; height: 2.8em; overflow: hidden; color: #222; }
  .product-summary { font-size: 0.9rem; color: #777; line-height: 1.5; margin-bottom: 15px; height: 3em; overflow: hidden; }

  /* 底部數值區 */
  .card-footer { 
    border-top: 1px dashed #eee; padding-top: 15px; margin-top: auto;
    display: flex; justify-content: space-between; align-items: center;
  }
  .price-text { color: #ff4d4f; font-weight: 800; font-size: 1.1rem; }
  .review-text { font-size: 0.8rem; color: #bbb; }

  .is-hidden { display: none !important; }
</style>

<div class="hero-banner">
  <h1 style="font-size: 3rem; margin: 0;">選品智庫 💡</h1>
  <p style="font-size: 1.1rem; opacity: 0.9;">每日為您精選最划算的購物與旅遊優惠</p>
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
        <div class="product-summary">{{ post.summary | truncate: 50 }}</div>
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
  // 切換按鈕樣式
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  // 過濾卡片
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