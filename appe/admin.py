from django.contrib import admin
from .models import Images

# Register your models here.

class AdminImages(admin.ModelAdmin):
    list_display = ['id','image_name','image']
admin.site.register(Images,AdminImages)