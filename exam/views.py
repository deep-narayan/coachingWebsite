from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from Prince_Institute.models import Student,Course
from .models import chapter,question,result
from django.contrib.auth.decorators import login_required

quest=""
# Create your views here.
@login_required
def home(request):
	selUser=User.objects.get(first_name=request.user.first_name)
	detail=Student.objects.get(user=selUser)
	course=Course.objects.all()
	chap=chapter.objects.all()
	return render(request,'techsel.html',{'n':selUser,'d':detail,'c':course,'ch':chap})


@login_required
def exam(request):
	
	technologyid=request.GET['techno']
	chapterid=request.GET['chapter']
	techname=Course.objects.get(id=technologyid)
	chapt=chapter.objects.get(id=chapterid)
	global quest
	quest=question.objects.filter(chapter=chapterid,tech=technologyid)
	return render(request,'giveexam.html',{'ques':quest,'name':techname.name,'t':techname,'c':chapt})


def quesres(request):
	res=0
	li={}
	length=0
	yourans=[]
	if request.method=='POST':
		ques_id=request.POST.getlist('quest')
		#print(ques_id)
		te=request.POST['t']
		ch=request.POST['c']
		techname=Course.objects.get(name=te)
		chapt=chapter.objects.get(chapter_name=ch)
		for i in ques_id:
			try:
				q1=request.POST['ans {}'.format(int(i))]
				li[i]=q1
			except:
				length+=1

		for i in li.keys():
			pqt=question.objects.get(id=i)
			newli=li[i].split()
			if pqt.correct==newli[0]:
				res+=1

		length+=len(li)

		usera=request.user
		marks=(res/length)*100
		r=result(user=usera,tech=techname,marks=marks,chapter=chapt)
		r.save()

		for z in ques_id:
			try:
				q1=request.POST['ans {}'.format(int(z))]
				ans=q1.split()
				yourans.append(ans[0])
			except:
				yourans.append("Not Done")
				

		global quest
		nques=zip(quest,yourans)
		return render(request,'quesans.html',{'nques':nques,'mark':marks})
	