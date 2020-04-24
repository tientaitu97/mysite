from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('blog/', views.post_list, name='post_list'),
    path('blog/<int:id>/', views.post_detail, name='post_detail'),
    path('blog/<int:id>/post_edit/', views.post_edit, name='post_edit'),
    path('blog/<int:id>/post_delete/', views.post_delete, name='post_delete'),
    path('post_create/', views.post_create, name='post_create'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),

    # Password_reset url's

    # url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'),
    # url(r'^password_reset/complete/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    url(r'^', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    url(r'^like/$', views.like_post, name="like_post"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
