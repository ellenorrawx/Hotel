from webbrowser import register

from django.contrib import admin
from.models import *
from modeltranslation.admin import TranslationAdmin

admin.site.register(Hotel)
admin.site.register(User)
admin.site.register(HotelPhoto)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Review)