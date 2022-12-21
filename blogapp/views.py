from django.shortcuts import redirect, render
from .models import blogs,profile_photo
from .forms import blogs_form, feedback_form
from django.contrib.auth.models import User ,auth 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.cache import cache_control
from django.contrib.auth import update_session_auth_hash


# Create your views here.
@cache_control(no_cashe=True,most_evalidate=True,no_store =True)
# @login_required(login_url='login')
def addblog (request):
    if request.method=='GET':
        form=blogs_form()
        return render(request ,'addblog.html',{'form':form})
    else:
        form=blogs_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

        return redirect('add')

@cache_control(no_cashe=True,most_evalidate=True,no_store =True)
def signup(request):
    if request.method =='GET':
        b= UserCreationForm
        return render(request,'signup.html',{'b':b})

    else :
        b = UserCreationForm(request.POST,request.FILES)
        if b.is_valid():
            b.save()
        return redirect('login')



@cache_control(no_cashe=True,most_evalidate=True,no_store =True)
def login(request):
    if request.method =='GET':
        login= AuthenticationForm(request)
        return render(request,'login.html',{'login':login})

    else :
        login = AuthenticationForm(request,data=request.POST)
        if login.is_valid():
            user=login.get_user()
            auth.login(request,user)
            return redirect('home')
        return redirect('login')

@cache_control(no_cashe=True,most_evalidate=True,no_store =True)
def logout(request):
    auth.logout(request)
    return redirect('login')

@cache_control(no_cashe=True,most_evalidate=True,no_store =True)
@login_required(login_url='login')
def home(request):
    data = blogs.objects.all()
    return render(request,'home.html',{'data':data})

@cache_control(no_cashe=True,most_evalidate=True,no_store =True)

@login_required(login_url='login')
def hollywood(request):
    return render(request ,'hollywood.html')
        
@cache_control(no_cashe=True,most_evalidate=True,no_store =True)

@login_required(login_url='login')
def about(request):
    return render(request ,'about.html')




def search(request):
    search=request.POST['search']
    if blogs.objects.filter(title__contains=search).exists():
        data = blogs.objects.filter(title__startswith=search)
        return render(request,'home.html',{'data':data})
    else:
        messages.info(request,"No Result Found")    
        return redirect('home')
@cache_control(no_cashe=True,most_evalidate=True,no_store =True)
    
@login_required(login_url='login')
def read(request,id):
    data = blogs.objects.get(id=id)
    print(data)
    return render(request,'readmore.html',{'i':data})




@cache_control(no_cashe=True,most_evalidate=True,no_store =True)

def feed (request):
    if request.method=='GET':
        form=feedback_form()
        return render(request ,'feedback.html',{'form':form})
    else:
        form=feedback_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

        return redirect('add')





def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})



def contact(request):
    return render(request ,'contact.html')


def add_profile_photo(request):
    if request.user.is_authenticated:
        if profile_photo.objects.filter(name__exact=request.user).exists():
            return redirect('profile')
        
        elif request.method == "POST":
            name = request.user
            profile = request.FILES['profile']
            profile_photo.objects.create(name=name,photo=profile)
            return redirect('profile')
        return render(request,'profile_photo.html')

    return redirect('login')


def profile(request):
    if profile_photo.objects.filter(name__exact=request.user).exists():
        data = profile_photo.objects.get(name__exact=request.user)
        return render (request,'profile.html',{'data':data})
    return render (request,'profile.html')

def update_profile(request,id):
    if request.user.is_authenticated:

        data = profile_photo.objects.get(id=id)

        if request.method == "POST":    
            profile = request.FILES['profile']

            a = profile_photo(id=id, name=data.name ,photo=profile)
            a.save()

            return redirect('profile')

        return render(request,'profile_photo.html',{'data':data})     

    return redirect('login')