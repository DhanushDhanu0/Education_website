from django.contrib import admin
from .models import Post,loginData


# Register your models here
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','date','info')
    list_display_links=('title',)
    list_filter =('id','is_published','author')
admin.site.register(Post, PostAdmin)

#logindata register
class loginDataAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','password')
    list_display_links=('username',)
    list_filter = ('id','username')
admin.site.register(loginData, loginDataAdmin)


