"""xiaomi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import os
from django.views.static import serve
from xiaomi.settings import BASE_DIR, MEDIA_ROOT
from xiaomi_views.views import index, login, register, addgouwuche, \
                                dingdan, liebiao, self_info, index1,\
                                search,showgouwuche
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index, name='index'),
    url(r'^user/', include('xiaomi_users.urls')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': os.path.join(BASE_DIR, 'static')}),
    url(r'^login/', login, name='login'),
    url(r'^register/', register, name='register'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^addgouwuche/', addgouwuche, name='addgouwuche'),
    url(r'^dingdan/', dingdan, name='dingdan'),
    url(r'^liebiao/', liebiao, name='liebiao'),
    url(r'^self_info/', self_info, name='self_info'),
    url(r'^index1/(?P<phone_id>\d+)$', index1, name='single_log'),
    url(r'^search/', search, name='search'),
    url(r'^showgouwuche/', showgouwuche, name='showgouwuche'),

]
