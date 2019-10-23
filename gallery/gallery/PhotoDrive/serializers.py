from rest_framework import serializers
from .models import User,Album,Photo

class UserListSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('username','first','last','profilepic','gender')

class UsernameSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('username','profilepic')

class UsernameAlbumSerializer(serializers.ModelSerializer):
	class Meta:
		model=Album
		fields=('username','album_id')

class UsernamePhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Photo
		fields=('photo_id','album_id')

class UserDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model=User
		fields=('username','first','last','profilepic','gender')

class UserUpdateSerializer(serializers.ModelSerializer):

	first=serializers.CharField(required=False)
	last=serializers.CharField(required=False)
	gender=serializers.CharField(required=False)
	email=serializers.CharField(required=False)
	password=serializers.CharField(required=False)

	class Meta:
		model=User
		fields=('first','last','gender','email','password')

class UserDeleteSerializer(serializers.ModelSerializer):

	class Meta:
		model=User
		fields= '__all__'

class UserCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model=User
		fields='__all__'

class AlbumListSerializer(serializers.ModelSerializer):
	class Meta:
		model=Album
		fields='__all__'

class AlbumUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model=Album
		fields=('description','cover','visibleTo','visible')

class AlbumDeleteSerializer(serializers.ModelSerializer):

	class Meta:
		model=Album
		fields= '__all__'

class AlbumCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model=Album
		fields=('album_id','description','cover')

	def create(self, validated_data):
		username = self.context['username']
		data = validated_data.copy()
		data['username'] = User.objects.get(username=username)
		return super(AlbumCreateSerializer, self).create(data)

class PhotoListSerializer(serializers.ModelSerializer):
	class Meta:
		model=Photo
		fields='__all__'

class PhotoDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model=Photo
		fields='__all__'

class PhotoUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model=Photo
		fields=('description','visibleTo','visible')


class PhotoDeleteSerializer(serializers.ModelSerializer):

	class Meta:
		model=Photo
		fields= '__all__'

class PhotoCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model=Photo
		fields=('photo_id','description','photo')

	def create(self, validated_data):
		album_id = self.context['album_id']
		data = validated_data.copy()
		data['album_id'] = Album.objects.get(album_id=album_id)
		return super(PhotoCreateSerializer, self).create(data)

class LikeAlbumSerializer(serializers.ModelSerializer):

	class Meta:
		model=Album
		fields=('liked',)

class LikePhotoSerializer(serializers.ModelSerializer):

	class Meta:
		model=Photo
		fields=('liked',)

class SetVisibleToAlbumSerializer(serializers.ModelSerializer):

	class Meta:
		model=Album
		fields=('visibleTo',)

class SetVisibleToPhotoSerializer(serializers.ModelSerializer):

	class Meta:
		model=Photo
		fields=('visibleTo',)

class SetVisiblityAlbumSerializer(serializers.ModelSerializer):

	class Meta:
		model=Album
		fields=('visible','album_id')

class SetVisiblityPhotoSerializer(serializers.ModelSerializer):

	class Meta:
		model=Photo
		fields=('visible','photo_id')
