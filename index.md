---
layout: default
title: 專業選品智庫 - 你的購物低價導航站
---

<div class="home-guide">
  <section class="hero-promo" style="background: #f4f4f4; padding: 40px; border-radius: 15px; margin-bottom: 30px; text-align: center; border: 2px solid #ee4d2d;">
    <h1 style="color: #ee4d2d;">🔥 今日限時：領取蝦皮商城免運券</h1>
    <p>專業選品家實測：搭配限時 5 折搶購，挑戰全網最低價！</p>
    <a href="https://afflnk.site/track/clicks/5282/c627c2bc980925d8fa83ec23d62e9e4524674ac163b2a0f90262ba0771401de3c021e7e5593c99616c" 
       target="_blank" 
       style="background: #ee4d2d; color: white; padding: 12px 30px; border-radius: 25px; text-decoration: none; font-weight: bold; display: inline-block;">
       立即前往領券中心
    </a>
  </section>

  <div class="category-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
    
    <section class="cat-section">
      <h2 style="border-left: 5px solid #ff4500; padding-left: 10px;">📉 低價促銷速報</h2>
      <ul style="list-style: none; padding: 0;">
        {% for post in site.tags.限時促銷 %}
        <li style="margin-bottom: 15px; border-bottom: 1px dashed #ccc; padding-bottom: 10px;">
          <a href="{{ post.url }}" style="font-weight: bold; text-decoration: none; color: #333;">{{ post.title }}</a>
          <div style="font-size: 0.9em; color: #666;">{{ post.summary }}</div>
        </li>
        {% endfor %}
      </ul>
    </section>

    <section class="cat-section">
      <h2 style="border-left: 5px solid #2e8b57; padding-left: 10px;">💆 專業頭皮養護</h2>
      <ul style="list-style: none; padding: 0;">
        {% for post in site.tags.頭皮護理 %}
        <li style="margin-bottom: 15px; border-bottom: 1px dashed #ccc; padding-bottom: 10px;">
          <a href="{{ post.url }}" style="font-weight: bold; text-decoration: none; color: #333;">{{ post.title }}</a>
          <div style="font-size: 0.9em; color: #666;">{{ post.summary }}</div>
        </li>
        {% endfor %}
      </ul>
    </section>

    <section class="cat-section">
      <h2 style="border-left: 5px solid #1e90ff; padding-left: 10px;">📱 科技生活選品</h2>
      <ul style="list-style: none; padding: 0;">
        {% for post in site.tags.居家選品 %}
        <li style="margin-bottom: 15px; border-bottom: 1px dashed #ccc; padding-bottom: 10px;">
          <a href="{{ post.url }}" style="font-weight: bold; text-decoration: none; color: #333;">{{ post.title }}</a>
          <div style="font-size: 0.9em; color: #666;">{{ post.summary }}</div>
        </li>
        {% endfor %}
      </ul>
    </section>

  </div>
</div>