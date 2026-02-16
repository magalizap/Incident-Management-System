from django import forms
from .models import Service, Incident, PostMortem

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'owner_team']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'owner_team': forms.TextInput(attrs={'class': 'form-control'}),
        }


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'description', 'service', 'severity', 'status', 'resolved_at']
        widgets = {
            'resolved_at': forms.DateInput(attrs={'type': 'date'}), 
            'description': forms.Textarea(attrs={'rows': 4}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'severity': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        

class PostMortemForm(forms.ModelForm):
    class Meta:
        model = PostMortem
        fields = ['incident', 'root_cause', 'impact', 'corrective_actions']
        widgets = {
            'root_cause': forms.Textarea(attrs={'rows': 4}),
            'impact': forms.Textarea(attrs={'rows': 4}),
            'corrective_actions': forms.Textarea(attrs={'rows': 4}),
            'incident': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['incident'].queryset = Incident.objects.filter(status='RESOLVED')
