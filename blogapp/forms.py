from django import forms
from .models import blogs, feedback



class blogs_form(forms.ModelForm):
    class Meta:
        model = blogs
        fields ='__all__'



class feedback_form(forms.ModelForm):
    class Meta:
        model = feedback
        fields ='__all__'
