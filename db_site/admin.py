from django.contrib import admin
from django.utils import timezone
from .models import Studio

# Register your models here.

class StudioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['name', 'url','country', 'region', 'language', 'is_active_comment']}),
        ('Social Media', {'fields':['twitter', 'facebook', 'instagram','youtube']}),
        ('Administrative', {'fields':['date_added', 'date_updated', 'is_approved', 'added_by', 'approved_by']}),
        ]
    def save_model(self, request, obj, form, change):
        obj.date_updated = timezone.now()
        super().save_model(request, obj, form, change)
admin.site.register(Studio, StudioAdmin)
