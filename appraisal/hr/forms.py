from .models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from hr.models import *
from django import forms
from django.db.models import Q
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Div
from crispy_forms import bootstrap, layout
from django.urls import reverse
from crispy_forms.layout import Layout, Submit


class EmployeeForm(forms.ModelForm):
    employee_first_name = forms.CharField(
        label='First Name',
        required=True
    )

    employee_middle_name = forms.CharField(
        label='Middle Name',
        required=True
    )
    employee_last_name = forms.CharField(
        label='Last Name',
        required=True
    )
    employee_username = forms.CharField(
        label='Username',
        required=True
    )
    employee_email=forms.EmailField(
        required=True,
        label='Employee Email'
    )

    employee_contact_no=forms.CharField(
        required=True,
        label='Contact Number'
    )

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('employee_first_name', css_class="col-sm-3"),
                    Div('employee_middle_name', css_class='col-sm-3'),
                    Div('employee_last_name', css_class="col-sm-3"),
                    Div('employee_username', css_class="col-sm-3"),
                    css_class='row'
                ),
                Div(
                    Div('employee_gender', css_class="col-sm-3"),
                    Div('employee_role', css_class='col-sm-3'),
                    Div('employee_email', css_class="col-sm-3"),
                    Div('employee_contact_no', css_class="col-sm-3"),

                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("employees")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = Employee
        fields = ['employee_first_name', 'employee_middle_name', 'employee_last_name', 'employee_username',
                  'employee_gender','employee_role', 'employee_email', 'employee_contact_no']

