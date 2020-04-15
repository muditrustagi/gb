from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import Item
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
	if request.user.is_authenticated:
		items=Item.objects.filter(username=request.user.username).order_by('-date')
		return render(request,'index.html',{'items':items})
	else:
		return redirect('/')

def userlogin(request):
	if request.user.is_authenticated:
		return redirect(index)
	else:
		return render(request,'userlogin.html')

def add(request):
	if request.user.is_authenticated:
		ite=Item()
		ite.name=request.POST['itemName']
		ite.qty=request.POST['qty']
		ite.status=request.POST['status']
		ite.date=request.POST['date']
		ite.username=request.user.username
		ite.save()
		return redirect('index')
	else:
		return redirect('/')

def login(request):
	if request.user.is_authenticated:
		return render(request,'login.html')
	else:
		return redirect('/')

def order(request):
	if request.user.is_authenticated:
		if request.META.get('HTTP_REFERER').split("/")[-1]=='index.html':
			print("true")
			fdate=request.POST['date']
			items=Item.objects.filter(date=fdate,username=request.user.username)
			if len(items)<=0:
				return render(request,'index.html',{'error':'No Entry Found','errorExists':True,'fdate':fdate})
			
			else:
				return render(request,'index.html',{'items':items,'fdate':fdate})
		else:
			return redirect('index')
	else:
		return redirect('/')

def update(request):
	if request.user.is_authenticated:
		itemId=request.GET['itemId']
		item=Item.objects.get(id=itemId)
		return render(request,'update.html', {'item':item})
	else:
		return redirect('/')

def viewupdate(request):
	itemId=request.POST['id']
	item=Item.objects.get(id=itemId)
	item.name=request.POST['itemName']
	item.qty=request.POST['qty']
	item.status=request.POST['status']
	item.date=request.POST['date']
	item.save()
	return redirect('index')

def delete(request):
	itemId=request.GET['itemId']
	ite=Item.objects.get(id=itemId)
	ite.delete()
	return redirect('index')

def error_404_view(request, exception):
    data = {"error": "404 Error Found"}
    return render(request,'error.html', data)

def error_500_view(request):
    data = {"error": "500 Error Found"}
    return render(request,'error.html', data)

def signup(request):
	return render(request,'signup.html')
	
		
def validateuser(request):
	user=auth.authenticate(username=request.POST['name'],password=request.POST['password'])
	if(user is not None):
		auth.login(request,user)
		return redirect('index')
	else:
		return render(request,'userlogin.html',{'errorExists':True,'error':'User not found'})

def validate(request):
	if User.objects.filter(username=request.POST['name']).exists():
		print(request.POST['name'])
		return render(request,'signup.html',{'errorExists':True,'error':'Username Taken'})
	elif request.POST['password']!=request.POST['confirmPassword']:
		return render(request,'signup.html',{'errorExists':True,'error':'Passwords do not match'})
	else:
		user=User.objects.create_user(username=request.POST['name'],password=request.POST['password'])
		user.save()
		auth.login(request,user)
		return redirect('index')
		

def logout(request):
	auth.logout(request)
	return redirect('/')
