from django.db import models

# Create your models here.
class blogarticle(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	title = models.CharField(max_length=255,default="", editable=True)
	story = models.CharField(max_length=9000)
	date = models.DateTimeField(auto_now_add=True)
	refid = models.CharField(max_length=5000,default="", editable=True)
	class Meta:
		db_table = "blogarticle"

# Create your comment model here
class comment(models.Model):
	refid = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	feedback = models.CharField(max_length=2000)
	story = models.CharField(max_length=9000,default="", editable=True)
	class Meta:
		db_table = "comment"
