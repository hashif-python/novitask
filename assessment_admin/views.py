from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login as dj_login


def adminlogin(request):
	if request.method =="POST":
		username = request.POST.get('username')
		password = request.POST.get('pass')
		user = authenticate(request, username = username, password = password)
		if user is not None and user.is_superuser:
			form = login(request, user)
			messages.success(request, f' Welcome {username} !!')
			return redirect('adminhome')
		else:
			messages.info(request, f'Account Does Not Exit!!!, Try Again')


	return render(request,'login.html')


@login_required
def adminhome(request):

	return render(request,'home.html')


def admin_logout_view(request):
    logout(request)
    return redirect('adminlogin')




@login_required
def view_products(request):
	ob5=Products.objects.all()





	context={

	'ob5':ob5
	}
	return render(request,'view_products.html',context)


@login_required
def add_products(request):

	if request.method == 'POST':

		item_name= request.POST.get('item_name')
		categ= request.POST.get('categ')
		price= request.POST.get('price')
		active= request.POST.get('active')
		image= request.FILES['image']
		status= request.POST.get("statusval")
		if status =="true":
		    active=True
		else:
		    active=False
		ob9=Products.objects.all()
		slno=len(ob9)+1
		ob=Products.objects.create(slno=slno,image=image,item_name=item_name,amount=price,is_active=active)
		ob.save()
		return redirect('view_products')

	context={
	
	}
	return render(request,'add_products.html',context)

@login_required
def edit_products(request,id):
    ob5=Products.objects.get(id=id)
    if request.method == 'POST':
        item_name= request.POST.get('item_name')
        price= request.POST.get('price')
        ob5.item_name=item_name
        ob5.amount=price
        ob5.save()
        try:
            image= request.FILES['image']
            if image:
               
                ob5.image=image
                ob5.save()
        except:
            pass





        status= request.POST.get("statusval")
        if status =="true":
            ob5.is_active = True
            ob5.save()
        elif status =="false":
            ob5.is_active = False
            ob5.save()

        

        return redirect('view_products')
    ob3=User.objects.get(username=request.user.username)
    context={
    'prod':ob5
    }
    return render(request,'add_products.html',context)


@login_required
def delete_products(request,id):
    ob2=Products.objects.get(id=id)
    ob3=Products.objects.all()
    ob2.delete()


    slno=0
    for i in ob3:
        slno+=1
        i.slno=slno
        i.save()

    return redirect('view_products')