from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Service, Incident, PostMortem

# Register your models here.

admin.site.unregister(User)
@admin.register(User)
class UserAdmin(BaseUserAdmin): 
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff') 
    search_fields = ('username', 'first_name', 'last_name', 'email') 
    readonly_fields = ('date_joined', 'last_login') 
    fieldsets = ( 
        (None, {'fields': ('username', 'password')}), 
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}), 
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}), 
        ('Important dates', {'fields': ('last_login', 'date_joined')}), 
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner_team', 'created_at')

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'service', 'severity', 'status', 'created_at', 'resolved_at')
    list_filter = ('status', 'severity')

@admin.register(PostMortem)
class PostMortemAdmin(admin.ModelAdmin):
    list_display = ('incident', 'root_cause', 'impact', 'corrective_actions', 'created_at')