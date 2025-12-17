---
layout: default
---

<div class="hero-header" style="
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('/assets/images/hero-bg.jpg');
    background-size: cover;
    background-position: center;
    padding: 80px 20px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
    border-radius: 10px;
">
    <h1 style="font-size: 2.5rem; margin-bottom: 10px;">選品智庫</h1>
    <p style="font-size: 1.2rem; opacity: 0.9;">AI 驅動的極致省錢術，為您過濾全球優質折扣</p>
</div>

## 📌 最新選品推薦

<div class="post-container">
  {% for post in site.posts %}
    <div style="border-bottom: 1px solid #eee; padding: 20px 0;">
      <small style="color: #888;">{{ post.date | date: "%Y-%m-%d" }}</small>
      <h3 style="margin: 10px 0;">
        <a href="{{ post.url | relative_url }}" style="color: #d32f2f; text-decoration: none;">{{ post.title }}</a>
      </h3>
      <p style="color: #555; font-size: 0.95rem;">{{ post.summary }}</p>
      <span style="background: #fff3e0; color: #e65100; padding: 2px 8px; border-radius: 4px; font-size: 0.85rem;">價格：{{ post.price }}</span>
    </div>
  {% endfor %}
</div>