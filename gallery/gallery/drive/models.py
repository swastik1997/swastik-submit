from django.db import models

def upload_to(instance, filename):
		return 'profilepic/%s/%s' % (instance.username, filename)

class User(models.Model):
	username=models.CharField(max_length=250,primary_key=True)
	first=models.CharField(max_length=250)
	last=models.CharField(max_length=250)
	email=models.CharField(max_length=250)
	gender=models.CharField(max_length=250)
	password=models.CharField(max_length=250)
	profilepic=models.ImageField(upload_to=upload_to,
		null=True,
		blank=True)

	def __str__(self):
		return self.username


def upload_to(instance, filename):
		return 'profilepic/%s/%s' % (instance.album_id, filename)

class Album(models.Model):
	album_id=models.CharField(primary_key=True,max_length=250)
	#username=models.ForeignKey(User,on_delete=models.CASCADE,related_name='album_owner'
	#	,default=0)
	description=models.CharField(max_length=250)
	date=models.DateTimeField(auto_now_add=True)
	liked=models.ManyToManyField(User,related_name='album',blank=True)
	visibleTo=models.ManyToManyField(User,related_name='album_visible',blank=True)
	directory=models.FileField(blank=True,null=True,upload_to=upload_to)
	cover=models.ImageField(upload_to=upload_to,
		null=True,
		blank=True)


def upload_to(instance, filename):
		return 'profilepic/%s/%s' % (instance.photo_id, filename)

class Photo(models.Model):
	photo_id=models.CharField(primary_key=True,max_length=250)
	album_id=models.ForeignKey(Album,on_delete=models.CASCADE,related_name='photo_album'
		,default=0)
	description=models.CharField(max_length=250)
	date=models.DateTimeField(auto_now_add=True)
	liked=models.ManyToManyField(User,related_name='photo',blank=True)
	visibleTo=models.ManyToManyField(User,related_name='photo_visible',blank=True)
	url=models.ImageField(upload_to=upload_to,
		null=True,
		blank=True,)



