---
layout: default
title: 選品智庫 - 全台最全優惠碼導航
---

<style>
  /* 導航按鈕樣式 */
  .category-nav {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin: 30px 0;
    flex-wrap: wrap;
  }
  .filter-btn {
    padding: 10px 24px;
    border-radius: 50px;
    border: 2px solid #f0f0f0;
    background: white;
    cursor: pointer;
    font-weight: 600;
    transition: 0.3s;
    font-size: 1rem;
    color: #555;
  }
  .filter-btn.active, .filter-btn:hover {
    background: #ff4d4f;
    color: white;
    border-color: #ff4d4f;
    box-shadow: 0 4px 12px rgba(255, 77, 79, 0.3);
  }

  /* 產品網格控制 */
  .shop-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 25px;
    padding: 10px;
  }

  /* 動態隱藏不符合分類的卡片 */
  .shop-card.hidden {
    display: none !important;
  }
</style>

<div class="hero-section" style="text-align: center; padding: 40px 0;">
  <h1>選品智庫 💡</h1>
  <p>每日更新，幫你從美食、旅遊到購物一網打盡！</p>
</div>

<div class="category-nav">
  <button class="filter-btn active" onclick="filterItems('all', this)">全部項目</button>
  <button class="filter-btn" onclick="filterItems('美食類', this)">🍕 美食優惠</button>
  <button class="filter-btn" onclick="filterItems('旅遊類', this)">✈️ 旅遊行程</button>
  <button class="filter-btn" onclick="filterItems('購物網站', this)">🛒 購物省錢</button>
</div>

<div id="product-grid" class="shop-grid">
  {% for post in site.posts %}
  {% assign cat = post.tags | first %}
  <div class="shop-card" data-category="{{ cat }}">
    <a href="{{ post.url }}">
      <div class="card-img" style="background-image: url('/assets/images/{{ post.filename | replace: ".md", "" }}.jpg'); height: 200px; background-size: cover; border-radius: 12px 12px 0 0;"></div>
      <div class="card-body" style="padding: 15px; border: 1px solid #eee; border-top: none; border-radius: 0 0 12px 12px;">
        <span class="badge" style="background: #fff2f0; color: #ff4d4f; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem;"># {{ cat }}</span>
        <h3 style="margin: 10px 0; font-size: 1.2rem;">{{ post.title }}</h3>
        <p style="color: #666; font-size: 0.9rem; height: 40px; overflow: hidden;">{{ post.summary | truncate: 50 }}</p>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px;">
          <span style="font-weight: bold; color: #ff4d4f; font-size: 1.1rem;">{{ post.price }}</span>
          <span style="font-size: 0.8rem; color: #999;">★ {{ post.rating }} ({{ post.reviews }} 評價)</span>
        </div>
      </div>
    </a>
  </div>
  {% endfor %}
</div>

<script>
function filterItems(category, btn) {
  // 1. 切換按鈕樣式
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  // 2. 顯示/隱藏卡片
  const cards = document.querySelectorAll('.shop-card');
  cards.forEach(card => {
    const cardCat = card.getAttribute('data-category');
    if (category === 'all' || cardCat === category) {
      card.classList.remove('hidden');
    } else {
      card.classList.add('hidden');
    }
  });
}
</script>