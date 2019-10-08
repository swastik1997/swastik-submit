from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

def upload_to(instance, filename):
		return 'profilepic/%s/%s' % (instance.username, filename)

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

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
		return 'cover/%s/%s' % (instance.album_id, filename)

class Album(models.Model):
	album_id=models.AutoField(primary_key=True)
	username=models.ForeignKey(User,on_delete=models.CASCADE,related_name='album_owner'
		,default=0)
	description=models.CharField(max_length=250)
	date=models.DateTimeField(auto_now_add=True)
	liked=models.ManyToManyField(User,related_name='album',blank=True)
	visibleTo=models.ManyToManyField(User,related_name='album_visible',blank=True)
	cover=models.ImageField(upload_to=upload_to,
		null=True,
		blank=True)
	visible=models.IntegerField(validators=[MinValueValidator(1),
		MaxValueValidator(3)],default=1)

	def __str__(self):
		return str(self.album_id)


def upload_to(instance, filename):
		return 'photo/%s' % ( filename)

class Photo(models.Model):
	photo_id=models.AutoField(primary_key=True)
	album_id=models.ForeignKey(Album,on_delete=models.CASCADE,related_name='photo_album')
	description=models.CharField(max_length=250)
	date=models.DateTimeField(auto_now_add=True)
	liked=models.ManyToManyField(User,related_name='photo',blank=True)
	visibleTo=models.ManyToManyField(User,related_name='photo_visible',blank=True)
	photo=models.ImageField(upload_to=upload_to,
		null=True,
		blank=True)
	visible=models.IntegerField(validators=[MinValueValidator(1),
		MaxValueValidator(3)],default=1)

	def __str__(self):
		return str(self.photo_id)



