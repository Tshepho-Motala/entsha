from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from .models import *

class JobForm(forms.ModelForm):
    class Meta:
        model = JobCart
        fields = ('fullname', 'id_no','job_type','job_description')
        labels = {
            'fullname': 'Full Names',
            'id_no': 'Identity number',
            'job_type': 'Job type',
            'job_description': 'Job Description',
            
            }

        def __init__(self, *args, **kwargs):
         super(JobForm, self).__init__(*args, **kwargs)
         self.fields['id_no'].required = False
