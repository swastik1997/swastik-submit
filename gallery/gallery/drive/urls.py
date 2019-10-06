from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	path('', views.UserList.as_view(),name="userlist"),
	path('<int:pk>/', views.UserDetail.as_view(),name="userdetail"),
	path('<int:pk>/edit/', views.UserUpdate.as_view(),name="userupdate"),
	path('<int:pk>/delete/', views.UserDelete.as_view(),name="userdelete"),
	path('create/', views.UserCreate.as_view(),name="usercreate"),
	path('<int:pk>/album/', views.AlbumList.as_view(),name="albumlist"),
]

urlpatterns = format_suffix_patterns(urlpatterns)