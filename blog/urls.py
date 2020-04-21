
from django.urls import path
from blog import views
urlpatterns = [

    path('blog', views.post_list, name='post_list'),
    path('blog/<int:id>', views.post_detail, name='post_detail'),
    path('post_create/', views.post_create, name='post_create'),
]