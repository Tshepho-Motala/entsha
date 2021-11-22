from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from .models import *

class DelphiusEmployeeForm(forms.ModelForm):

    class Meta:
        model = Delphius_Employee
        fields = ('fullname', 'lastname','id_no','emp_code','position',  )
        labels = {
            'fullname': 'Full Names',
            'lastname': 'Last Name',
            'id_no': 'Identity Number',
            'emp_code': 'Employee code',
            'position': 'Position',
            }

        def __init__(self, *args, **kwargs):
         super(DelphiusEmployeeForm, self).__init__(*args, **kwargs)
         self.fields['position'].empty_label = "Select"
         self.fields['emp_code'].required = False


class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = fields = ('site', 'cont_person','cont_no', 'address', 'region', 'status', 
                           'employee', 'started', 'expected', 'verified', 'action')
        labels = {
            'site': 'Site',
            'cont_person': 'Contact Person',
            'cont_no': 'Contact Number',
            'address': 'Address',
            'region': 'Region',
            'status': 'Status',
            'employee': 'Brought by',
            'started': 'Started date',
            'expected': 'Expected date',
            'verified': 'Verified date',
            'action': 'Action date',
            
            }
    def __init__(self, *args, **kwargs):
        super(LeadForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "Select"
        self.fields['employee'].empty_label = "Select"
        self.fields['cont_no'].required = False


class interest_Form(forms.ModelForm):
    class Meta:
        model = Delphius_interest
        fields = ('site_name', 'cont_person','cont_no', 'address', 'region', 'latitude', 'longitude',
                 'solution_type', 'est_duration', 'p_participation', 'participation', 'municipal_appr', 'est_municipal', 
                 'est_power_conn', 'dusk_dawn', 'delconn_interest', 'solution_sh', 'est_solu_cost', 'operator_interest', 
                 )
        labels = {
            'site_name': 'Site Name',
            'cont_person': 'Lead Contact Person',
            'cont_no': 'Lead Contact Number',
            'address': 'Lead Address',
            'region': 'Lead Region',
            'latitude': 'Lead Latitude',
            'longitude': 'Lead Longitude',
            'solution_type': 'Solution Type Requested',
            'est_duration': 'Estimated Duration of Public Participation in days',
            'p_participation': 'Public Participation required',
            'participation': 'Public Participation Likelihood',
            'municipal_appr': 'Municipal Approval Required',
            'est_municipal': 'Estimated Municipal in days',
            'est_power_conn': 'Power Connection Estimate',
            'dusk_dawn': 'Dawn to Dusk Estimate',
            'delconn_interest': 'Del Connect Interested',
            'solution_sh': 'Solution Sheareable',
            'est_solu_cost': 'Estimated Solution Cost',
            'operator_interest': 'Operator Interest',
            
            
            }

