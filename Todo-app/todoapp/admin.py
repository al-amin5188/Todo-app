from django.contrib import admin
from todoapp.models import TodoApp

# Register your models here.
class TodoAppAdmin(admin.ModelAdmin):
    list_display=('title','detels','time')


admin.site.register(TodoApp, TodoAppAdmin)