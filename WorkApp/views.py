from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *

def Main(request):
	return render(request, 'main.html')


def Feedback(request):
	return render(request, 'Fdbk.html')

def Register(request):
	if request.method == "POST":
		Alastname = request.POST['Alastname']
		Afirstname = request.POST['Afirstname']
		Amiddlename = request.POST['Amiddlename']
		Abday = request.POST['Abday']
		Aemailadd = request.POST['Aemailadd']
		Acontactnum = request.POST['Acontactnum']
		person = Personal(
		Alastname = Alastname,
		Afirstname = Afirstname,
		Amiddlename = Amiddlename,
		Abday = Abday,
		Aemailadd = Aemailadd,
		Acontactnum = Acontactnum,
)
		person.save()
		messages.info(request,"ThankYou for Register!")
	else:
		return render(request,'LogReg.html')
	reg = Personal.objects.all()
	return render(request,'LogReg.html',{'reg':reg})

def Delete_Register(request,thid):
	person =Personal.objects.get(id =thid)
	person.delete()
	return render(request,'main.html')

def Edit_Reg(request,thid):
	Reg_info_edit =Personal.objects.get(id = thid)
	reg = Personal.objects.all()
	return render(request,'LogReg.html',{'Reg_info_edit':Reg_info_edit,
		'reg':reg,
		})

def Update_reg(request,thid):
	reg = Personal.objects.get(id = thid)
	reg.Alastname = request.POST['Alastname']
	reg.Afirstname = request.POST['Afirstname']
	reg.Amiddlename = request.POST['Amiddlename']
	reg.Abday = request.POST['Abday']
	reg.Aemailadd = request.POST['Aemailadd']
	reg.Acontactnum = request.POST['Acontactnum']
	reg.save()
	return redirect('Register')

def Jobs(request):
	return render(request, 'job.html')

def Aboutus(request):
	return render(request, 'about.html')

def Sampleresume(request):
	return render(request, 'job.html')

def Tips(request):
	return render(request, 'tps.html')

def TableReg(request):
	reg = Personal.objects.all()
	return render(request, 'regtable.html',{'reg':reg})

'''	if request.method == 'POST':
		Oname = request.POST['FullName']
		Oemail = request.POST['Email']
		Ophonenumber = request.POST['PhoneNumber']
		Ogender = request.POST['Gender']
		Oage = request.POST['Age']
		Personal.objects.create(Aname=Oname,Aemail=Oemail,Aphonenumber=Ophonenumber,Agender=Ogender,
			Aage=Oage)
		return redirect('/')

	Mylist = Personal.objects.all()'''
	
		