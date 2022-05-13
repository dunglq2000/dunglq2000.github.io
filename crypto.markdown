---
layout: page
title: Crypto
permalink: /crypto/
---

<div markdown="2">
	{% for post in site.posts %}
		{% if post.tags contains "cryptography" %}
			<div class="post-link-wrapper">
	      	<a href="{{ post.url | relative_url }}" class="post-link">{{ post.title }}</a>
	      	<div class="post-meta">
	        	{% if site.plugins contains "jekyll/tagging" %}
	        	<div class="post-tags">
	            {% for tag in post.tags %}
	            <a class="tag" href="{{ tag | tag_url }}">{{ tag }}</a>
	            {% endfor %}
	        </div>
	        {% endif %}
	        {% if site.dash.date_format %}
	          {{ post.date | date: site.dash.date_format }}
	        {% else %}
	          {{ post.date | date: "%b %-d, %Y" }}
	        {% endif %}
	        {% if site.show_excerpts == true %}
	          <div class="post-excerpt">
	            {{ post.content | strip_html | truncatewords: 50 }}
	          </div>
	        {% endif %}
	      </div>
	    </div>
		{% endif %}
	{% endfor %}
</div>