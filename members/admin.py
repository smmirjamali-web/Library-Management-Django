from django.contrib import admin
from . models import Member

# Register your models here.
@admin.register(Member)
class MermberAdmin(admin.ModelAdmin):
    list_display = ['user', 'national_id', 'phone', 'user_type', 'is_active', 'joined_at']
    list_filter = ['user_type', 'is_active']
    search_fields = ['national_id', 'phone', 'user__first_name', 'user__last_name', 'user__username']
    