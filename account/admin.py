from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import *

class UserAdmin(UserAdmin):
    model = User
    list_display = ('name', 'phone_number', 'id_number', 'role')
    search_fields = ('name', 'phone_number', 'id_number', 'role')
    ordering = ('id',)

admin.site.register(User, UserAdmin)
admin.site.register(Role)