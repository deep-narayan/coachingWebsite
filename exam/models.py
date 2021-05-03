from django.db import models
from django.contrib.auth.models import User
from Prince_Institute.models import Course



class chapter(models.Model):
	def __str__(self):
		return self.chapter_name

	technology=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
	chapter_name=models.CharField(max_length=200)

class question(models.Model):
	def __str__(self):
		return self.question
	question=models.TextField(max_length=500,unique=True)
	optiona=models.CharField(max_length=50)
	optionb=models.CharField(max_length=50)
	optionc=models.CharField(max_length=50)
	optiond=models.CharField(max_length=50)
	correct=models.CharField(max_length=10)
	tech = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
	chapter=models.ForeignKey(chapter,on_delete=models.DO_NOTHING)

class result(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	tech = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
	chapter=models.ForeignKey(chapter,on_delete=models.DO_NOTHING)
	marks=models.CharField(max_length=10)
	date=models.DateTimeField(auto_now_add=True)



