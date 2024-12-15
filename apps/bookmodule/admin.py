from django.contrib import admin

# Register your models here.
#lab 10 task 1
# from .models import Address

# admin.site.register(Address)

#lab 10 task 2
from .models import Address2, Student2

admin.site.register(Address2)
admin.site.register(Student2)
