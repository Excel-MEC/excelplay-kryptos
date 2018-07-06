from django.db import models

# Create your models here.

class User(models.Model):
	user_id = models.CharField(primary_key=True,max_length=100)
	username = models.CharField(max_length=100)
	profile_picture = models.URLField()
	email = models.EmailField()
	
	def __str__(self):
		return self.username

class Level(models.Model):
    #options = (
    #    ('A', 'Audio'),
    #    ('I', 'Image'),
    #    ('G', 'Gif'),
    #)
	level = models.IntegerField(default =1)
	answer = models.TextField()
	source_hint = models.TextField(blank=True,null=True)
	#level_file =  models.FileField(upload_to = 'level_images/',null=True)
	#filetype = models.CharField(max_length = 10,choices=options,default='Audio')
	def __str__(self):
		return str(self.level)

class KryptosUser(models.Model):
    # TODO: Bring user ID from auth
    user_id = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    rank = models.IntegerField(default=10000)

    def __str__(self):
        return str(self.rank)