from django.contrib import admin
from . models import User, Panchayath, Panchayath_details, Muncipality, Muncipality_details, Corporation, Corporation_details

# Register your models here.
admin.site.register(User)
admin.site.register(Panchayath)
admin.site.register(Panchayath_details)
admin.site.register(Muncipality)
admin.site.register(Muncipality_details)
admin.site.register(Corporation)
admin.site.register(Corporation_details)
