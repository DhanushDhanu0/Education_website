from django.shortcuts import render,redirect
from .models import Post,loginData

# Create your views here.
def Home(request):
    return render(request,'index.html')


def About(request):
    return render(request,'about.html')

def Gallery(request):
    return render(request,'gallery.html')

def Courses(request):
    return render(request,'courses.html')

def Testmonials(request):
    return render(request,'testmonials.html')

def Signin(request):
    return render(request,'signin.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        data = loginData(username = username, email = email, password = password)
        data.save()
        redirect('/')
    return render(request,'login.html')


def Blog(request):
    posts = Post.objects.all()
    context = {
         'posts':posts,
        
    }
    
    return render(request,'blog.html',context)



     