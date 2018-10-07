from django.db import models

# Create your models here.

class User(models.Model):
	#TODO: User model to be imported from core auth
	user_id = models.CharField(primary_key=True,max_length=100)
	username = models.CharField(max_length=100)
	profile_picture = models.URLField()
	email = models.EmailField()
	points = models.IntegerField(default=0)

	def __repr__(self):
		return self.username
	class Meta:
		ordering = ['user_id','points']



class Level(models.Model):
	options = (
	   ('A', 'Audio'),
	   ('I', 'Image'),
	   ('G', 'Gif'),
	)
	level = models.IntegerField(default =1)
	answer = models.TextField()
	source_hint = models.TextField(blank=True,null=True)
	level_file =  models.FileField(upload_to = 'level_images/',null=True)
	filetype = models.CharField(max_length = 10,choices=options,default='Audio')
	def __str__(self):
		return str(self.level)

class KryptosUser(models.Model):
	user_id = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
	level = models.IntegerField(default=1)
	rank = models.IntegerField(default=10000)
	last_anstime = models.DateTimeField()

	def __str__(self):
		return str(self.rank)


class SubmittedAnswer(models.Model):
	kryptosUser = models.ForeignKey(KryptosUser, on_delete=models.CASCADE)
	answers = models.TextField()
