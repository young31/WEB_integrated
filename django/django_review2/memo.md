in base url
{% if user in article.liked_users.all %}
<a href="{% url 'articles:like' article.pk %}"><i class="fas fa-heart fa-xs" style="color:red"></i><br></a>
{% else %}
<a href="{% url 'articles:like' article.pk %}"><i class="far fa-heart fa-xs" style="color:red"></i><br></a>
{% endif %}