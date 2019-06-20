from django.contrib import admin
from .models import post
# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug' ,'published' ,'status')
    list_filter  = ('title', 'published' ,'status')
    search_fields= ('title', 'body')
    ordering = ['status', 'published']  
    prepopulated_fields = {'slug' : ('title',)}
admin.site.register(post,postAdmin)