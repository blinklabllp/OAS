from django import forms
from .models import ClientPrimaryUser, ClientTeamMember, ProjectManager, Artist


class ClientPrimaryUserForm(forms.ModelForm):
    class Meta:
        model = ClientPrimaryUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'company_name', 'address_line1', 'address_line2', 'city', 'state', 'zip_code']


class ClientTeamMemberForm(forms.ModelForm):
    class Meta:
        model = ClientTeamMember
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class ProjectManagerForm(forms.ModelForm):
    class Meta:
        model = ProjectManager
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['first_name', 'last_name', 'email', 'phone_number']
