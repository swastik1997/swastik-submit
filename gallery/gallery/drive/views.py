from django.shortcuts import render,get_object_or_404 
from django.http import HttpResponse
from .models import User,Album,Photo
from django.template import loader
from django.http import Http404
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	DestroyAPIView,
	CreateAPIView
	)
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)
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
	)
#from .permissions import IsOwnerOrReadOnly

class UserList(ListAPIView):

	queryset=User.objects.all()
	serializer_class=UserListSerializer

class UserDetail(RetrieveAPIView):

	queryset=User.objects.all()
	serializer_class=UserDetailSerializer

class UserDelete(DestroyAPIView):

	queryset=User.objects.all()
	serializer_class=UserDeleteSerializer

class UserUpdate(UpdateAPIView):

	queryset=User.objects.all()
	serializer_class=UserUpdateSerializer
	permission_classes=[IsAuthenticatedOrReadOnly]

class UserCreate(CreateAPIView):

	queryset=User.objects.all()
	serializer_class=UserCreateSerializer
	permission_classes=[IsAuthenticated,IsAdminUser]

class AlbumList(ListAPIView):

	queryset=User.objects.all()
	serializer_class=AlbumListSerializer
	def get_queryset(self):
		user = str(self.request.user)
		return Album.objects.filter(user_id=user)

class AlbumDelete(DestroyAPIView):

	queryset=User.objects.all()
	serializer_class=AlbumDeleteSerializer


class AlbumUpdate(UpdateAPIView):

	serializer_class=AlbumUpdateSerializer
	permission_classes=[IsAuthenticatedOrReadOnly]
	def get_queryset(self):
		uid = self.kwargs.get(self.lookup_url_kwarg)
		albums = Album.objects.filter(album_id=uid)
		return albums

class AlbumCreate(CreateAPIView):

	queryset=User.objects.all()
	serializer_class=AlbumCreateSerializer
	permission_classes=[IsAuthenticated,IsAdminUser]






