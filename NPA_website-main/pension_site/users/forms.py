from django import forms
from .models import UserProfile,Notification,District, Taluka,UserLocation

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'phone', 'bio', 'age', 'designation']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
        }

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter community message...'}),
        }

class LocationForm(forms.Form):
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label="Select District", widget=forms.Select(attrs={'class': 'form-control'}))
    taluka = forms.ModelChoiceField(queryset=Taluka.objects.none(), empty_label="Select Taluka", widget=forms.Select(attrs={'class': 'form-control'}))