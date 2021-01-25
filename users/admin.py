from django.contrib import admin

# Register your models here.

class MyAdmin(admin.ModelAdmin):
     def has_add_permission(self, request, obj=None):
        return False