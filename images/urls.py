from django.urls import  path

from images import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'image_share.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path('', views.upload, name = "main"),
    path('handl/', views.hnd_load, name = "handl"),
]
