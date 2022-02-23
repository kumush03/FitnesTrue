from django.contrib import admin

# # Register your models here.

# from contact.models import Contact

# admin.site.register(Contact)
from django.contrib import admin
from contact.models import Contact
# Register your models here.
class Conractadmin(admin.ModelAdmin):
    list_display = ("name","email", "adress","message","sent_at")


admin.site.register(Contact)