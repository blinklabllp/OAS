from django.contrib import admin
from .models import ClientPrimaryUser, ClientTeamMember, ProjectManager, Artist


@admin.register(ClientPrimaryUser)
class ClientPrimaryUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'company_name', 'phone_number', 'active']
    search_fields = ['username', 'email', 'company_name', 'phone_number']
    list_filter = ['active']


@admin.register(ClientTeamMember)
class ClientTeamMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email', 'phone_number', 'active']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']
    list_filter = ['active']
    raw_id_fields = ['user']


@admin.register(ProjectManager)
class ProjectManagerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'active']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']
    list_filter = ['active']


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'active']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']
    list_filter = ['active']
