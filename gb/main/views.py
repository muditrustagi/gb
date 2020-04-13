from django.shortcuts import render

from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
	items=Item.objects.all().order_by('-date')
	return render(request,'index.html',{'items':items})

def add(request):
	ite=Item()
	ite.name=request.POST['itemName']
	ite.qty=request.POST['qty']
	ite.status=request.POST['status']
	ite.date=request.POST['date']
	ite.save()

	items=Item.objects.all().order_by('-date')
	return render(request,'index.html',{'items':items})

def login(request):
	return render(request,'login.html')

def order(request):
	fdate=request.POST['date']
	items=Item.objects.filter(date=fdate)
	return render(request,'index.html',{'items':items,'fdate':fdate})
	
def update(request):
	itemId=request.GET['itemId']
	item=Item.objects.get(id=itemId)
	return render(request,'update.html', {'item':item})

def viewupdate(request):
	itemId=request.POST['id']
	item=Item.objects.get(id=itemId)
	item.name=request.POST['itemName']
	item.qty=request.POST['qty']
	item.status=request.POST['status']
	item.date=request.POST['date']
	item.save()
	items=Item.objects.all().order_by('-date')
	return render(request,'index.html',{'items':items})

def delete(request):
	itemId=request.GET['itemId']
	ite=Item.objects.get(id=itemId)
	ite.delete()
	items=Item.objects.all().order_by('-date')
	return render(request,'index.html',{'items':items})