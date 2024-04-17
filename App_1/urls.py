from django.urls import path
from .views import Home,About,Gallery,Courses,Testmonials,Signin,Login,Blog

urlpatterns = [
    path('',Home,name="home"),
    path('about',About,name="about"),
    path('gallery',Gallery,name="gallery"),
    path('courses',Courses,name="courses"),
    path('testmonials',Testmonials,name="testmonials"),
    path('signin',Signin,name="signin"),
    path('login',Login,name="login"),
    path('blog',Blog,name="blog"),
]