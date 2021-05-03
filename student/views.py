from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from Prince_Institute.models import Course,Student,Fee
from exam.models import result,chapter

# Create your views here.
def studenthome(request):
	try:
		selUser=User.objects.get(first_name=request.user.first_name)
		detail=Student.objects.get(user=selUser)

	except:
		error="Username or Password Incorrect!!"
		return render(request,'error.html',{'error':error}) 

	return render(request,'dashboard.html',{'n':selUser,'d':detail})



def viewcertificate(request):
	selUser=User.objects.get(first_name=request.user.first_name)
	detail=Student.objects.get(user=selUser)

	return render(request,'certificate.html',{'n':selUser,'d':detail})


def resultview(request):
	selUser=User.objects.get(first_name=request.user.first_name)
	detail=Student.objects.get(user=selUser)
	res=result.objects.filter(user=selUser.id)


	return render(request,'results.html',{'n':selUser,'d':detail,'obj':res})

def feeview(request):
	selUser=User.objects.get(first_name=request.user.first_name)
	detail=Student.objects.get(user=selUser)

	f=Fee.objects.filter(student=selUser)
	
	return render(request,'fee.html',{'n':selUser,'d':detail,'fee':f})


