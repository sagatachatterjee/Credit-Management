from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import user_detail,transaction
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
ids=0
def index(request):
	return render(request,'creditManage/index.html',{})

def view_usr(request):
	all_entries=user_detail.objects.all()
	detail_send={"data":all_entries}
	return render(request,'creditManage/view_usr.html',detail_send)

def view_trans(request):
	all_entries=transaction.objects.all()
	detail_send={"data":all_entries}
	return render(request,'creditManage/view_trans.html',detail_send)

def transfer(request):
	all_entries=user_detail.objects.all()
	detail_send={"data":all_entries}
	return render(request,'creditManage/transfer.html',detail_send)

def transfer_to(request):
	all_entries=user_detail.objects.all()
	detail_send={"data":all_entries}
	return render(request,'creditManage/transfer_to.html',detail_send)

@csrf_exempt
def detail1(request):
	print(" hello")
	t_from=""
	t_to=""
	if(request.POST):
		print(" hello1")
		print(request.POST)
		c=request.POST.get('id')
		c1=request.POST.get('credit')
		print(type(c1))
		all_entries=user_detail.objects.all()
		for i in all_entries:
			print("hola")
			if(i.id==ids):
				if(i.credit>=int(c1)):
					print (i.credit)
					user_detail.objects.filter(id=i.id).update(credit=i.credit-int(c1))
					t_from=i.name
				else:
					return HttpResponse('error')
			if(i.id==int(c)):
				print("hh")
				user_detail.objects.filter(id=i.id).update(credit=i.credit+int(c1))
				t_to=i.name
		uu=transaction.objects.create(trac_from=t_from,trac_to=t_to,credit=int(c1))	
		
	return HttpResponse('success')

@csrf_exempt
def detail(request):
	global ids
	print(" hello")
	if(request.POST):
		print(" hello1")
		print(request.POST)
		c=request.POST.get('id')
		all_entries=user_detail.objects.all()
		for i in all_entries:
			print("hola")
			if(i.id==int(c)):
				ids=i.id
				print("hh")

	return HttpResponse('success')
