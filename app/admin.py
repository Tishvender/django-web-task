from django.contrib import admin
from app.models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','contact','email_department']