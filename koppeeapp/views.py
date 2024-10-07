from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required




# Create your views here.
def index(request):
    menu1= Menu.objects.filter(category='Hot Coffee')
    menu2= Menu.objects.filter(category='Cold Coffee')

    context={
        'services':Services.objects.all(),
        'menu':{
            'hot':menu1,
            'cold':menu2
        },
        'clients':Client.objects.all()
    }
    return render(request, 'design/index.html',context)


def about(request):
    context={
        'teams':Team.objects.all()
    }
    return render(request, 'design/about.html',context)

def services(request):
    context={
        'services':Services.objects.all()
    }
    return render(request, 'design/services.html',context)

def menu(request):
    menu1= Menu.objects.filter(category='Hot Coffee')
    menu2= Menu.objects.filter(category='Cold Coffee')
    context={
        'menu':{
            'hot':menu1,
            'cold':menu2
        }
    }
    return render(request,'design/menu.html',context)

# @login_required
# def reservation(request):
#     if request.method=="POST":
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         phone=request.POST.get('phone')
#         date=request.POST.get('date')
#         time=request.POST.get('time')
#         person=request.POST.get('person')
#         message=request.POST.get('message')
#         reservation=Reservation(name=name,email=email,phone=phone,date=date,time=time,number_of_guest=person,message=message)
#         reservation.save()
#         messages.success(request,"Reservation successful")
#         return redirect('/reservation')
#     else:
#         messages.success(request,"Reservation Failed")
#         return render(request,'design/reservation.html')
#     return render(request,'design/reservation.html')



from django.shortcuts import render, redirect
from .forms import ReservationForm

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the reservation if the form is valid
            return redirect('/')  # Redirect to a success page
    else:
        form = ReservationForm()  # Create an empty form for GET requests

    return render(request, 'design/reservation.html', {'form': form})

def testimonials(request):
    context={
        'clients':Client.objects.all()
    }

    return render(request,'design/testimonials.html',context)

def contact(request):
    return render(request,'design/contacts.html')




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'User Created Successfully.')
            return redirect('/')
        else:
            messages.add_message(request,messages.ERROR,'Error 401✖️')
            return render(request,'accounts/register.html',{'Forms':form})


    context ={
        'Forms': UserCreationForm()
    }
    return render(request,'accounts/register.html',context)


def userLogin(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username = data['username'], password = data['password'])
            if user is not None:
                login(request,user) 
            else:
                messages.add_message(request,messages.ERROR,"Invalid Credentials.")
                return render(request,'accounts/login.html',{'Forms':form})

    context= {
        'Forms': LoginForm()
    }
    return render(request,'accounts/login.html',context)


def userLogout(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'User Logout')
    return redirect('/')

        
