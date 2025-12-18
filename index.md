---
layout: default
title: 選品智庫 - 全台最全優惠導航
---

<style>
  :root { --primary-red: #ff4d4f; --bg-gray: #f8f9fa; --text-dark: #262626; }
  body { background-color: var(--bg-gray); color: var(--text-dark); }

  /* 分類導航列優化 */
  .filter-nav { display: flex; justify-content: center; gap: 12px; margin: 40px 0; flex-wrap: wrap; }
  .btn-filter { 
    padding: 10px 28px; border-radius: 50px; border: 1px solid #ddd; 
    background: white; cursor: pointer; font-weight: 500; transition: 0.3s;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  }
  .btn-filter.active { background: var(--primary-red); color: white; border-color: var(--primary-red); }

  /* 產品網格系統 */
  .product-grid { 
    display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); 
    gap: 30px; max-width: 1200px; margin: 0 auto; padding: 0 20px;
  }

  /* 精緻卡片設計 */
  .card-item { 
    background: white; border-radius: 16px; overflow: hidden; 
    transition: transform 0.3s, box-shadow 0.3s; text-decoration: none !important; color: inherit;
    display: flex; flex-direction: column; height: 100%; border: 1px solid #efefef;
  }
  .card-item:hover { transform: translateY(-8px); box-shadow: 0 15px 30px rgba(0,0,0,0.1); }

  .card-thumb { 
    width: 100%; aspect-ratio: 16/9; background-size: contain; 
    background-repeat: no-repeat; background-position: center; 
    background-color: #fff; border-bottom: 1px solid #f0f0f0; padding: 20px;
  }
  
  .card-content { padding: 20px; flex-grow: 1; display: flex; flex-direction: column; }
  .tag-cat { color: var(--primary-red); font-size: 0.8rem; font-weight: bold; margin-bottom: 8px; }
  .card-title { font-size: 1.15rem; font-weight: 600; line-height: 1.4; margin-bottom: 12px; height: 3.2em; overflow: hidden; }
  .card-desc { font-size: 0.9rem; color: #666; line-height: 1.6; margin-bottom: 20px; flex-grow: 1; }
  
  .card-meta { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f5f5f5; padding-top: 15px; }
  .price-info { font-weight: bold; color: var(--primary-red); font-size: 1.1rem; }
  .rating-info { font-size: 0.85rem; color: #8c8c8c; }

  .hidden { display: none !important; }
</style>

<div style="text-align: center; padding: 60px 20px 20px;">
  <h1 style="font-size: 2.5rem; margin-bottom: 15px;">選品智庫 💡</h1>
  <p style="color: #666;">精選美食、旅遊、購物優惠，每日為您更新最優選內容</p>
</div>

<div class="filter-nav">
  <button class="btn-filter active" onclick="filterItems('all', this)">全部項目</button>
  <button class="btn-filter" onclick="filterItems('美食類', this)">🍕 美食優惠</button>
  <button class="btn-filter" onclick="filterItems('旅遊類', this)">✈️ 旅遊行程</button>
  <button class="btn-filter" onclick="filterItems('購物網站', this)">🛒 購物省錢</button>
</div>

<div class="product-grid" id="mainGrid">
  {% for post in site.posts %}
  {% assign cat = post.tags | first %}
  <div class="card-item-wrap" data-cat="{{ cat }}">
    <a href="{{ post.url }}" class="card-item">
      <div class="card-thumb" style="background-image: url('/assets/images/{{ post.filename | replace: '.md', '' }}.jpg'), url('/assets/images/{{ post.filename | replace: '.md', '' }}.png');"></div>
      <div class="card-content">
        <div class="tag-cat"># {{ cat }}</div>
        <h3 class="card-title">{{ post.title }}</h3>
        <p class="card-desc">{{ post.summary | truncate: 60 }}</p>
        <div class="card-meta">
          <span class="price-info">{{ post.price }}</span>
          <span class="rating-info">★ {{ post.rating }} ({{ post.reviews }})</span>
        </div>
      </div>
    </a>
  </div>
  {% endfor %}
</div>

<script>
function filterItems(category, btn) {
  document.querySelectorAll('.btn-filter').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  const items = document.querySelectorAll('.card-item-wrap');
  items.forEach(item => {
    if (category === 'all' || item.getAttribute('data-cat') === category) {
      item.classList.remove('hidden');
    } else {
      item.classList.add('hidden');
    }
  });
}
</script>