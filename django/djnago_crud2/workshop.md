```python
  {% for comment in comments %}
    <li>{{ comment.pk }}. {{ comment.content }}</li>
    <form action="{% url 'articles:comments_delete' article.pk  comment.pk %}" method="POST">
      {% csrf_token %}
      <button type="submit">삭제하기</button>
    </form>
    {% empty %}
      <p>아직 댓글이 없습니다...</p>
  {% endfor %}
```

