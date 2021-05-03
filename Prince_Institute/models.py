from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
	def __str__(self):
		return self.name

	name=models.CharField(max_length=20,unique=True)
	price=models.DecimalField(max_digits=15, decimal_places=2)
	duration=models.CharField(max_length=10)
	discription=models.CharField(max_length=100)

class Student(models.Model):
	class Meta():
		unique_together = ('user', 'aadhar')
			
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	father_name = models.CharField(max_length=50)
	mother_name = models.CharField(max_length=50)
	mobileno = models.CharField(max_length=15)
	father_mob= models.CharField(max_length=15)
	dob=models.CharField(max_length=15) 
	gender=models.CharField(max_length=10)
	address=models.CharField(max_length=200)
	aadhar=models.CharField(max_length=20)
	pcourse=models.CharField(max_length=10)
	course=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
	photo = models.ImageField(upload_to='student_profile', blank=True)


class Fee(models.Model):
	def __str__(self):
		return self.student.first_name
	course=course=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
	student=models.ForeignKey(User, on_delete=models.CASCADE)
	paid_fee=models.DecimalField(max_digits=15, decimal_places=2)
	due=models.DecimalField(max_digits=15, decimal_places=2)
	status=models.IntegerField()
	date=models.DateTimeField(auto_now_add=True)


class MessageRequest(models.Model):
	def __str__(self):
		return self.message
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=20)
	message=models.TextField(max_length=500)
		