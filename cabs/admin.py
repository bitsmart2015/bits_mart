
from django.contrib import admin
from models import *
# class OfferAdmin(admin.ModelAdmin):
# 	list_display = ('room', 'bhavan','vacancy')
admin.site.register(CabOffer)
# admin.site.register(Room, RoomAdmin)
# admin.site.register(Category)

# Register your models here.
