from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as PhotoDrive_views

urlpatterns = [
	path('', 
		PhotoDrive_views.UserList.as_view(),name="userlist"),

	path('login/', 
		PhotoDrive_views.login,name="login"),

	path('logout/', 
		PhotoDrive_views.logout,name="logout"),

	path('<str:username>/detail/', 
		PhotoDrive_views.UserDetail.as_view(),name="userdetail"),

	path('<str:username>/edit/', 
		PhotoDrive_views.CanUserUpdate,name="userupdate"),

	path('<str:username>/delete/', 
		PhotoDrive_views.CanUserDelete,name="userdelete"),

	path('create/', 
		PhotoDrive_views.UserCreate.as_view(),name="usercreate"),

	path('<str:username>/', 
		PhotoDrive_views.AlbumList.as_view(),name="albumlist"),

	path('<str:username>/<int:album_id>/edit/', 
		PhotoDrive_views.CanAlbumUpdate,name="albumupdate"),

	path('<str:username>/<int:album_id>/delete/', 
		PhotoDrive_views.CanAlbumDelete,name="albumdelete"),

	path('<str:username>/<int:album_id>/like/', 
		PhotoDrive_views.likealbum,name="likealbum"),

	path('<str:username>/<int:album_id>/<int:photo_id>/like/', 
		PhotoDrive_views.likephoto,name="likephoto"),

	path('<str:username>/<int:album_id>/setvisibleto/', 
		PhotoDrive_views.CanSetVisibleToAlbum,name="setvisibletoalbum"),

	path('<str:username>/<int:album_id>/<int:photo_id>/setvisibleto/', 
		PhotoDrive_views.CanSetVisibleToPhoto,name="setvisibletophoto"),

	path('<str:username>/<int:album_id>/setvisiblity/', 
		PhotoDrive_views.CanSetVisiblityAlbum,name="setvisiblityalbum"),

	path('<str:username>/<int:album_id>/<int:photo_id>/setvisiblity/', 
		PhotoDrive_views.CanSetVisiblityPhoto,name="setvisiblityphoto"),

	path('<str:username>/create/', 
		PhotoDrive_views.CanAlbumCreate,name="albumcreate"),

	path('<str:username>/<int:album_id>/', 
		PhotoDrive_views.PhotoList.as_view(),name="photolist"),

	path('<str:username>/<int:album_id>/<int:photo_id>/', 
		PhotoDrive_views.PhotoDetail.as_view(),name="photodetail"),

	path('<str:username>/<int:album_id>/<int:photo_id>/edit/', 
		PhotoDrive_views.CanPhotoUpdate,name="photoupdate"),

	path('<str:username>/<int:album_id>/<int:photo_id>/delete/', 
		PhotoDrive_views.CanPhotoDelete,name="photodelete"),

	path('<str:username>/<int:album_id>/create/', 
		PhotoDrive_views.CanPhotoCreate,name="photocreate"),
]

urlpatterns = format_suffix_patterns(urlpatterns)