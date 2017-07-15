from django import forms
from rango.models import UserInformation,ConnectionDetail

class UserInformationForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text="Please enter your name")
    uniqueid = forms.CharField(max_length=128,help_text="Please enter your uniqueid")
    email = forms.CharField(max_length=128,help_text="Please enter your Email")
    emailpass = forms.CharField(max_length=128,help_text="Please enter your Email password")
    fbkey = forms.CharField(max_length=128,help_text="Please enter your fbkey")

    class Meta:
        model = UserInformation
        fields = ('name','uniqueid','email','emailpass','fbkey',)

class ConnectionDetailForm(forms.ModelForm):
    uniqueid = forms.CharField(max_length=128,help_text="Please enter your uniqueid")
    pcid = forms.CharField(widget=forms.HiddenInput())
    appid = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = ConnectionDetail
        fields = ('uniqueid',)
