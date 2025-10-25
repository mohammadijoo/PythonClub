from django.contrib import admin
from .models import Todo
from .models import Project

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


# Register your models here.
admin.site.register(Todo, TodoAdmin)

admin.site.register(Project)
