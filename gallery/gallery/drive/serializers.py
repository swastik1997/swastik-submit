from rest_framework import serializers
from .models import User,Album,Photo

class UserListSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('username','first','last','profilepic')

class UserDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model=User
		fields=('username','first','last','profilepic')

class UserUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model=User
		fields=('first','last','profilepic','gender','email','password')

class UserDeleteSerializer(serializers.ModelSerializer):

	class Meta:
		model=User
		fields= '__all__'

class UserCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model=User
		fields=('username','first','last','profilepic','gender','email','password')

class AlbumListSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields='__all__'

class AlbumUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model=User
		fields='__all__'

class AlbumDeleteSerializer(serializers.ModelSerializer):

	class Meta:
		model=User
		fields= '__all__'

class AlbumCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model=User
		fields='__all__'







