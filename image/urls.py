"""image URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,  include

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

admin.autodiscover()

MEDIA_ROOT =r'C:\Users\DELL\imageshare\media'
MEDIA_URL = 'media/'
urlpatterns = [
    # Examples:
    # url(r'^$', 'image_share.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('', include('images.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
# urlpatterns += patterns('',
#         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#         'document_root': settings.MEDIA_ROOT}))
