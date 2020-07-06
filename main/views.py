from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import CreateUserForm,profile_form
from .models import Profile
from .decorator import allowed_user
from django.contrib.auth.decorators import login_required

 
@login_required(login_url='login_signup')
def dashboard(request):
    context={}
    return render(request,'dashboard.html',context)
# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user is not None:
            print('True')
            login(request,user)
            
            place = Profile.objects.get(user=user)
            

            x=str(place.id)
            
            return redirect('../profile/'+x+'/')
        else:
            messages.info(request,'Usernaame Or Password is not correct')
    context={}

    return redirect('login_signup')
def logoutUser(request):
    logout(request)
    return redirect('login_signup')
def login_signup_page(request):
    form=CreateUserForm()
    role=request.POST.get('role')
    
    if request.method == 'POST' :
        
        
        print(request.POST)
        
        form=CreateUserForm(request.POST)
        if form.is_valid():

            user = form.save()
            if role == '1':
                group=Group.objects.get(name='Employee')
                user.groups.add(group)
            elif role=='0':
                group=Group.objects.get(name='Developer')
                user.groups.add(group)
            Profile.objects.create(
                user=user,
                )
        


            
    
    context={'form':form}
    
    return render(request,'login_signup.html',context)
@login_required(login_url='login_signup')
@allowed_user(allowed_roles=['Employee','Developer'])
def E_profile(request):
    user=request.user.profile
    print(request.user.profile.id)
    form=profile_form(instance=user)
    if request.method == 'POST':
        form = profile_form(request.POST, request.FILES, instance=user)
        if form.is_valid():
            print("save")
            form.save()
       
            

        x=str(request.user.profile.id)
            
        return redirect('../profile/'+x+'/')
    context={'form':form}
    return render(request,'Edit_profile.html',context)



@login_required(login_url='login_signup')
@allowed_user(allowed_roles=['Employee','Developer'])
def profile(request,pk_test):
    pk_test=int(pk_test)
    profile=Profile.objects.get(id=pk_test)
    context={'profile':profile}
    return render(request,'profile.html',context)