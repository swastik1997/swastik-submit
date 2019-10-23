from django.shortcuts import render,get_object_or_404 
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from .models import User,Album,Photo
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
	)
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import (
	UserListSerializer,
	UserDetailSerializer,
	UserDeleteSerializer,
	UserUpdateSerializer,
	UserCreateSerializer,
	AlbumListSerializer,
	AlbumDeleteSerializer,
	AlbumUpdateSerializer,
	AlbumCreateSerializer,
	PhotoListSerializer,
	PhotoDetailSerializer,
	PhotoDeleteSerializer,
	PhotoUpdateSerializer,
	PhotoCreateSerializer,
	LikeAlbumSerializer,
	LikePhotoSerializer,
	SetVisibleToAlbumSerializer,
	SetVisibleToPhotoSerializer,
	SetVisiblityAlbumSerializer,
	SetVisiblityPhotoSerializer,
	UsernameSerializer,
	UsernameAlbumSerializer,
	UsernamePhotoSerializer,
	)
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
	return render(request,'login.html')

def register(request):
	return render(request,'register.html')

def home_user(request):
	return render(request,'home.html')

def home_album(request):
	return render(request,'album.html')

def home_create_album(request):
	return render(request,'createAlbum.html')

def home_create_photo(request):
	return render(request,'createPhoto.html')

def home_edit_user(request):
	return render(request,'editUser.html')

def home_edit_album(request):
	return render(request,'editAlbum.html')

def home_edit_photo(request):
	return render(request,'editPhoto.html')

def home_photo(request):
	return render(request,'photo.html')

def logout(request):
	if request.method == 'GET':
		del request.session['username']
		return HttpResponseRedirect('../../')
	else:
		return HttpResponseNotFound('<h1>Page not found</h1>')

def login(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		user=User.objects.filter(username=username)
		if not user:
			return HttpResponseNotFound('<h1>Page not found</h1>')
		psw=User.objects.get(username=username).password
		if psw==request.POST.get('password'):
			request.session['username']=username
			return HttpResponseRedirect('../home/')
		else:
			return HttpResponseRedirect('../../')
	else:
		return HttpResponseNotFound('<h1>Page not found</h1>')

def isOwner(request,username):
	if username==request.session['username']:
		return HttpResponse(json.dumps({'bool': "true"}), content_type="application/json")
	return HttpResponse(json.dumps({'bool': "false"}), content_type="application/json")

class Username(RetrieveAPIView):
	
	serializer_class=UsernameSerializer

	def get_queryset(self):
		username=self.request.session['username']
		return User.objects.filter(username=username)

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(queryset,username=self.request.session['username'])
		return obj

class UsernameAlbum(RetrieveAPIView):
	
	serializer_class=UsernameAlbumSerializer

	def get_queryset(self):
		album_id=self.kwargs['album_id']
		return Album.objects.filter(album_id=album_id)

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(queryset,album_id=self.kwargs['album_id'])
		return obj

class UsernamePhoto(RetrieveAPIView):
	
	serializer_class=UsernamePhotoSerializer

	def get_queryset(self):
		photo_id=self.kwargs['photo_id']
		return Photo.objects.filter(photo_id=photo_id)

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(queryset,photo_id=self.kwargs['photo_id'])
		return obj

class UserList(ListAPIView):

	queryset=User.objects.all()
	serializer_class=UserListSerializer

class UserDetail(RetrieveAPIView):

	queryset=User.objects.all()
	serializer_class=UserDetailSerializer
	lookup_field='username'
	def get_queryset(self):
		username = self.kwargs['username']
		return User.objects.filter(username=username)

class UserDelete(DestroyAPIView):

	queryset=User.objects.all()
	serializer_class=UserDeleteSerializer
	lookup_field='username'

class UserUpdate(UpdateAPIView):

	queryset=User.objects.all()
	serializer_class=UserUpdateSerializer
	lookup_field='username'

	def update(self, request, *args, **kwargs):
		response = super(UserUpdate, self).update(request, *args, **kwargs)
		return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/PhotoDrive/home/')

class UserCreate(CreateAPIView):

	queryset=User.objects.all()
	serializer_class=UserCreateSerializer

	def create(self, request, *args, **kwargs):
		response = super(UserCreate, self).create(request, *args, **kwargs)
		return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/')

def likealbum(request,username,album_id):

	user=request.session['username']
	album=Album.objects.get(album_id=album_id)
	liked=album.liked.filter(username=user)
	if not liked:
		album.liked.add(User.objects.get(username=user))
	return HttpResponseRedirect('../')


def likephoto(request,photo_id,username,album_id):

	photo=Photo.objects.get(photo_id=photo_id)
	liked=photo.liked.filter(username=request.session['username'])
	if not liked:
		photo.liked.add(User.objects.get(username=request.session['username']))
	return HttpResponseRedirect('../')

def CanSetVisibleToAlbum(request,username,album_id):

	if username==request.session['username']:
		return SetVisibleToAlbum.as_view()(request,username=username,album_id=album_id)
	else:
		return HttpResponseRedirect('../')

def CanSetVisibleToPhoto(request,username,album_id,photo_id):

	if username==request.session['username']:
		return SetVisibleToPhoto.as_view()(request,username=username,album_id=album_id,photo_id=photo_id)
	else:
		return HttpResponseRedirect('../')

def CanSetVisiblityAlbum(request,username,album_id):

	if username==request.session['username']:
		return SetVisiblityAlbum.as_view()(request,username=username,album_id=album_id)
	else:
		return HttpResponseRedirect('../')

def CanSetVisiblityPhoto(request,username,album_id,photo_id):

	if username==request.session['username']:
		return SetVisiblityPhoto.as_view()(request,username=username,album_id=album_id,photo_id=photo_id)
	else:
		return HttpResponseRedirect('../')

def CanAlbumCreate(request,username):

	if username==request.session['username']:
		return AlbumCreate.as_view()(request,username=username)
	else:
		return HttpResponseRedirect('../')

@csrf_exempt
def CanAlbumUpdate(request,username,album_id):

	request.method=request.POST.get('_method')
	if username==request.session['username']:
		return AlbumUpdate.as_view()(request,username=username,album_id=album_id)
	else:
		return HttpResponseRedirect('../')

@csrf_exempt
def CanAlbumDelete(request,username,album_id):

	if username==request.session['username']:
		return AlbumDelete.as_view()(request,username=username,album_id=album_id)
	else:
		return HttpResponseRedirect('../')
		
def CanPhotoCreate(request,username,album_id):

	if username==request.session['username']:
		return PhotoCreate.as_view()(request,username=username,album_id=album_id)
	else:
		return HttpResponseRedirect('../')

@csrf_exempt
def CanPhotoUpdate(request,username,album_id,photo_id):

	request.method=request.POST.get('_method')
	if username==request.session['username']:
		return PhotoUpdate.as_view()(request,username=username,album_id=album_id,photo_id=photo_id)
	else:
		return HttpResponseRedirect('../')

@csrf_exempt
def CanPhotoDelete(request,username,album_id,photo_id):

	if username==request.session['username']:
		return PhotoDelete.as_view()(request,username=username,album_id=album_id,photo_id=photo_id)
	else:
		return HttpResponseRedirect('../')

@csrf_exempt
def CanUserUpdate(request,username):

	request.method=request.POST.get('_method')
	if username==request.session['username']:
		return UserUpdate.as_view()(request,username=username)
	else:
		return HttpResponseRedirect('../')

def CanUserDelete(request,username):

	if username==request.session['username']:
		return UserDelete.as_view()(request,username=username)
	else:
		return HttpResponseRedirect('../')

class SetVisibleToAlbum(UpdateAPIView):

	queryset=Album.objects.all()
	serializer_class=SetVisibleToAlbumSerializer
	lookup_field='album_id'
	def get_queryset(self):
		album_id = self.kwargs['album_id']
		return Album.objects.filter(album_id=album_id)

class SetVisibleToPhoto(UpdateAPIView):

	queryset=Photo.objects.all()
	serializer_class=SetVisibleToPhotoSerializer
	lookup_field='photo_id'
	def get_queryset(self):
		photo_id = self.kwargs['photo_id']
		return Photo.objects.filter(photo_id=photo_id)

class SetVisiblityAlbum(UpdateAPIView):

	queryset=Album.objects.all()
	serializer_class=SetVisiblityAlbumSerializer
	lookup_field='album_id'
	def get_queryset(self):
		album_id = self.kwargs['album_id']
		return Album.objects.filter(album_id=album_id)

class SetVisiblityPhoto(UpdateAPIView):

	queryset=Photo.objects.all()
	serializer_class=SetVisiblityPhotoSerializer
	lookup_field='photo_id'
	def get_queryset(self):
		photo_id = self.kwargs['photo_id']
		return Photo.objects.filter(photo_id=photo_id)


class AlbumList(ListAPIView):

	serializer_class=AlbumListSerializer
	lookup_field='username'
	def get_queryset(self):
		user=self.request.session['username']
		username = self.kwargs['username']
		if(username==user):
			return Album.objects.filter(username=username)
		queryset=Album.objects.filter(username=username)
		queryset1=queryset.filter(visible=1)
		queryset2=queryset.filter(visible=3)
		queryset2=queryset.filter(visibleTo=User.objects.get(username=user))
		return queryset1|queryset2

class AlbumDelete(DestroyAPIView):

	queryset=Album.objects.all()
	serializer_class=AlbumDeleteSerializer
	lookup_field='album_id'


class AlbumUpdate(UpdateAPIView):

	queryset=Album.objects.all()
	serializer_class=AlbumUpdateSerializer
	lookup_field='album_id'

	def update(self, request, *args, **kwargs):
		response = super(AlbumUpdate, self).update(request, *args, **kwargs)
		return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/PhotoDrive/home/album/?albumId='+str(self.kwargs['album_id']))

class AlbumCreate(CreateAPIView):

	queryset=Album.objects.all()
	serializer_class=AlbumCreateSerializer
	lookup_field='username'

	def get_serializer_context(self):
		context = super().get_serializer_context()
		context.update(
			{
				"username": self.request.session['username']
			}
		)
		return context

	def create(self, request, *args, **kwargs):
		response = super(AlbumCreate, self).create(request, *args, **kwargs)
		return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/PhotoDrive/home/')

class PhotoList(ListAPIView):

	serializer_class=PhotoListSerializer
	lookup_field='album_id'
	def get_queryset(self):
		user=self.request.session['username']
		album_id = self.kwargs['album_id']
		username = self.kwargs['username']
		if(username==user):
			return Photo.objects.filter(album_id=album_id)
		if Album.objects.get(album_id=album_id).visible == 1:
			queryset=Photo.objects.filter(album_id=album_id)
			queryset1=queryset.filter(visible=1)
			queryset2=queryset.filter(visible=3)
			queryset2=queryset.filter(visibleTo=User.objects.get(username=user))
			return queryset1|queryset2
		if Album.objects.get(album_id=album_id).visible == 3:
			if (Album.objects.get(album_id=album_id).visibleTo).get(username=user)==User.objects.get(username=user):
				queryset=Photo.objects.filter(album_id=album_id)
				queryset1=queryset.filter(visible=1)
				queryset2=queryset.filter(visible=3)
				queryset2=queryset.filter(visibleTo=User.objects.get(username=user))
				return queryset1|queryset2
		return Photo.objects.filter(photo_id=0)

class PhotoDetail(RetrieveAPIView):

	serializer_class=PhotoDetailSerializer
	lookup_field='photo_id'
	def get_queryset(self):
		user=self.request.session['username']
		username = self.kwargs['username']
		photo_id = self.kwargs['photo_id']
		if(username==user):
			return Photo.objects.filter(photo_id=photo_id)
		if Photo.objects.get(photo_id=photo_id).visible == 1:
			return Photo.objects.filter(photo_id=photo_id)
		if Photo.objects.get(photo_id=photo_id).visible == 3:
			queryset=Photo.objects.filter(photo_id=photo_id)
			queryset=queryset.filter(visibleTo=User.objects.get(username=user))
			return queryset
		return Photo.objects.none()

class PhotoDelete(DestroyAPIView):

	queryset=Photo.objects.all()
	serializer_class=PhotoDeleteSerializer
	lookup_field='photo_id'


class PhotoUpdate(UpdateAPIView):

	queryset=Photo.objects.all()
	serializer_class=PhotoUpdateSerializer
	lookup_field='photo_id'

	def update(self, request, *args, **kwargs):
		response = super(PhotoUpdate, self).update(request, *args, **kwargs)
		return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/PhotoDrive/home/photo/?photoId='+str(self.kwargs['photo_id']))

class PhotoCreate(CreateAPIView):

	queryset=Photo.objects.all()
	serializer_class=PhotoCreateSerializer
	lookup_field='album_id'
	def get_serializer_context(self):
		context = super().get_serializer_context()
		context.update(
			{
				"album_id": self.kwargs['album_id']
			}
		)
		return context

	def create(self, request, *args, **kwargs):
		response = super(PhotoCreate, self).create(request, *args, **kwargs)
		return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/PhotoDrive/home/album/?albumId='+str(self.kwargs['album_id']))
