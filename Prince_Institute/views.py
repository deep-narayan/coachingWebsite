from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Course,Student,Fee,MessageRequest
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core import mail
from .settings import context_dict


def home(request):
	if request.method=='POST':
		nm=request.POST['pname']
		mail=request.POST['email']
		contact=request.POST['number']
		mess=request.POST['message']

		m=MessageRequest(name=nm,email=mail,mobile=contact,message=mess)
		m.save()
		send_mail('Name:{}'.format(nm),'Message:{} From Email:{} From contact: {} '.format(mess,mail,contact),'aupadhydy007@gmail.com',['atul05794@gmail.com',email],fail_silently=False)
		return render(request,'index.html',{'sent':"Your Query Submitted"})

	return render(request,'index.html')


def contact(request):
	if request.method=='POST':
		nm=request.POST['pname']
		mail=request.POST['email']
		contact=request.POST['number']
		mess=request.POST['message']

		m=MessageRequest(name=nm,email=mail,mobile=contact,message=mess)
		m.save()
		#send_mail('Name:{}'.format(nm),'Message:{} From Email:{} From contact: {} '.format(mess,mail,contact),'aupadhydy007@gmail.com',['atul05794@gmail.com'],fail_silently=False)
		return render(request,'contact.html',{'sent':"Your Query Submitted"})
	return render(request,'contact.html')

def login_call(request):
	if request.method=='POST':
		u=request.POST['username']
		p=request.POST['password']
		try:
			selUser = authenticate(username=u, password=p)
			#print(selUser)
		except:
			return render(request,'error.html')

		if selUser:
			if selUser.is_superuser:
				login(request, selUser)
				return redirect('/submitfee/')
			else:
				login(request, selUser)
				return redirect('/student/home')


	return render(request,'login.html')

def submitfee(request):
	err=""
	fees=""
	u=User.objects.all()
	c=Course.objects.all()
	if request.method=='POST':
		cour=request.POST['course']
		stud=request.POST['student']
		try:
			fees=Fee.objects.filter(course=cour,student=stud)
		except:
			err="Student Did not Register or Wrong Details"
		finally:	
			return render(request,'duefee.html',{'f':fees,'error':err,'course':cour,'student':stud})


	return render(request,'submitfee.html',{'users':u,'course':c})

def finalfee(request):
	sta=0
	if request.method=='POST':
		stud=request.POST['student']
		cour=request.POST['course']
		paid=request.POST['paidfee']
		duef=request.POST['duefee']
		#print(duef)

		if duef=='0.00':
			sta=1
		u=User.objects.get(id=stud)
		c=Course.objects.get(id=cour)
		
		#f=Fee.objects.filter(student=u,course=c).update(paid_fee=paid,due=duef,status=sta)
		f=Fee(student=u,course=c,paid_fee=paid,due=duef,status=sta)
		f.save()

	return render(request,'feereceipt.html',{'fee':f})

def logout_call(request):
	logout(request)
	return redirect('/login/')

def register(request):
	username=[]
	user=User.objects.all()
	course=Course.objects.all()
	for i in user:
		username.append(i.username)
	if request.method=='POST':
		fname=request.POST['nm1']
		lname=request.POST['nm2']
		username=request.POST['username']
		password=request.POST['pwd']
		email=request.POST['email']
		add=request.POST['add']
		dateob=request.POST['dob']
		gender=request.POST['gender']
		faname=request.POST['faname']
		moname=request.POST['moname']
		cont=request.POST['mobileno']
		fnum=request.POST['fatherno']
		aadharno=request.POST['aadharnum']
		course=request.POST['course']
		pic=request.FILES['photu']
		
		course_id=Course.objects.get(id=int(course))

		#print(fnum)
		#print(aadharno)
		#print(cont)

		try:
			u=User(first_name=fname,last_name=lname,email=email,username=username,password=make_password(password))
			u.save()

			s=Student(user=u,gender=gender,dob=dateob,address=add,father_name=faname,mother_name=moname,mobileno=cont,father_mob=fnum,aadhar=aadharno,pcourse='no',course=course_id,photo=pic)
			s.save()

			#send_mail('subject:','Message ','from',['to'],fail_silently=False)

		except:
			error="User Already Exist!"
			return render(request,'error.html',{'error':error})


		return render(request,'regreceipt.html',{'user':u,'stu':s})
		
	return render(request,'register.html',{'course':course,'username':username})


def gallery(request):
	newfile=[]
	s=""
	for i in context_dict['files']:
		s='dynamicimage/{}'.format(i)
		newfile.append(s)
	print(newfile[0])

	return render(request, 'gallery.html',{'files':newfile})

def courses(request):
	return render(request,'course.html')

def faculty(request):
	return render(request,'faculty.html')

def about(request):
	return render(request,'about.html')