---
layout: default
title: 選品智庫 - 你的購物低價導航站
---

<div class="home-guide">
  <section class="hero-promo" style="background: #fff; padding: 40px; border-radius: 15px; margin-bottom: 30px; text-align: center; border: 2px solid #ff5722; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
    <h1 style="color: #ff5722; margin-top: 0;">🔥 今日限時：領取蝦皮商城免運券</h1>
    <p style="color: #666; font-size: 1.1em;">專業選品家實測：搭配限時 5 折搶購，帶你掌握全網最低價！</p>
    <a href="https://afflnk.site/track/clicks/5282/c627c2bc980925d8fa83ec23d62e9e4524674ac163b2a0f90262ba0771401de3c021e7e5593c99616c" 
       target="_blank" 
       style="background: #ff5722; color: white; padding: 15px 40px; border-radius: 30px; text-decoration: none; font-weight: bold; display: inline-block; font-size: 1.2em; transition: transform 0.2s;">
       立即前往領券中心
    </a>
  </section>

  <div class="category-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px;">
    
    <section class="cat-section" style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
      <h2 style="border-left: 5px solid #ff5722; padding-left: 10px; color: #333; margin-bottom: 20px;">📉 低價促銷速報</h2>
      <ul style="list-style: none; padding: 0;">
        {% for post in site.tags.限時促銷 %}
        <li style="margin-bottom: 20px; border-bottom: 1px dashed #eee; padding-bottom: 15px;">
          <a href="{{ post.url }}" style="font-weight: bold; text-decoration: none; color: #ff5722; font-size: 1.1em; display: block; margin-bottom: 5px;">{{ post.title }}</a>
          <div style="font-size: 0.9em; color: #666; line-height: 1.5;">{{ post.summary }}</div>
        </li>
        {% endfor %}
      </ul>
    </section>

    <section class="cat-section" style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
      <h2 style="border-left: 5px solid #4CAF50; padding-left: 10px; color: #333; margin-bottom: 20px;">💆 專業頭皮養護</h2>
      <ul style="list-style: none; padding: 0;">
        {% for post in site.tags.頭皮護理 %}
        <li style="margin-bottom: 20px; border-bottom: 1px dashed #eee; padding-bottom: 15px;">
          <a href="{{ post.url }}" style="font-weight: bold; text-decoration: none; color: #4CAF50; font-size: 1.1em; display: block; margin-bottom: 5px;">{{ post.title }}</a>
          <div style="font-size: 0.9em; color: #666; line-height: 1.5;">{{ post.summary }}</div>
        </li>
        {% endfor %}
      </ul>
    </section>

    <section class="cat-section" style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
      <h2 style="border-left: 5px solid #2196F3; padding-left: 10px; color: #333; margin-bottom: 20px;">📱 科技生活選品</h2>
      <ul style="list-style: none; padding: 0;">
        {% for post in site.tags.居家選品 %}
        <li style="margin-bottom: 20px; border-bottom: 1px dashed #eee; padding-bottom: 15px;">
          <a href="{{ post.url }}" style="font-weight: bold; text-decoration: none; color: #2196F3; font-size: 1.1em; display: block; margin-bottom: 5px;">{{ post.title }}</a>
          <div style="font-size: 0.9em; color: #666; line-height: 1.5;">{{ post.summary }}</div>
        </li>
        {% endfor %}
      </ul>
    </section>

  </div>
</div>