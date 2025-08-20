from django.contrib import admin

# Register your models here.
from .models import Lost, Found

class Lost_read_only(admin.ModelAdmin):
    readonly_fields = ('created',)

class Found_read_only(admin.ModelAdmin):
    readonly_fields = ('created',)

# Register your models here.

admin.site.register(Lost, Lost_read_only)
admin.site.register(Found, Found_read_only)