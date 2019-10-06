from django.contrib import admin
from django.urls import path, re_path, include
from PhotoDrive import views 
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('PhotoDrive/', include('PhotoDrive.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home,name="home"),
]

if settings.DEBUG:
	urlpatterns+=[
		re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,}),
	]