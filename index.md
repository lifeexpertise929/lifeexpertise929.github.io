<style>
  /* 專業標籤 CSS */
  .badge {
    position: absolute;
    top: 10px;
    left: 10px;
    background: #ff4d4f;
    color: white;
    padding: 3px 10px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: bold;
    z-index: 10;
  }
  
  .stars {
    color: #fadb14;
    font-size: 0.8rem;
    margin-top: 5px;
  }
</style>

<div class="post-grid">
  {% for post in site.posts %}
  <a href="{{ post.url }}" class="post-card" style="position: relative;">
    {% if post.badge %}
    <div class="badge">{{ post.badge }}</div>
    {% endif %}

    <div class="card-preview" style="background-image: url('/assets/images/{{ post.id | split: "/" | last }}.jpg');">
      </div>
    
    <div class="card-content">
      <span class="card-tag"># {{ post.tags | first }}</span>
      <div class="card-title">{{ post.title }}</div>
      
      <div class="stars">
        ★ {{ post.rating | default: "4.5" }} <span style="color:#999">(100+ 評價)</span>
      </div>
      
      <p class="card-summary" style="margin-top:10px;">{{ post.summary }}</p>
    </div>
    
    <div class="card-footer">
      <span class="card-price">💰 {{ post.price }}</span>
      <span class="card-more">立即領取 →</span>
    </div>
  </a>
  {% endfor %}
</div>