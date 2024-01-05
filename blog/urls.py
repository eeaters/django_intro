from django.urls import path, include
from . import views

urlpatterns = [
    path('hello_world', views.hello_world),
    path('article_content', views.article_content),
    path('index', views.get_index_page),
    path('detail/<int:article_id>', views.get_detail_page)
]
