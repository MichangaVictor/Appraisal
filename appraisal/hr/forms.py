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
    employee_email = forms.EmailField(
        required=True,
        label='Employee Email'
    )

    employee_contact_no = forms.CharField(
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
                            f'<a href="{reverse("employee")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = Employee
        fields = ['employee_first_name', 'employee_middle_name', 'employee_last_name', 'employee_username',
                  'employee_gender', 'employee_role', 'employee_email', 'employee_contact_no']


class DesignationForm(forms.ModelForm):
    designation_code = forms.CharField(
        label='Designation Code',
        required=True
    )
    designation_name = forms.CharField(
        label='Designation Name',
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(DesignationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('designation_code', css_class="col-sm-3"),
                    Div('designation_name', css_class='col-sm-9'),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("designation")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = Designation
        fields = ['designation_code', 'designation_name']


class MinistryForm(forms.ModelForm):
    ministry_code = forms.CharField(
        label='Ministry Code',
        required=True
    )
    ministry_name = forms.CharField(
        label='Ministry Name',
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(MinistryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('ministry_code', css_class="col-sm-3"),
                    Div('ministry_name', css_class='col-sm-9'),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("ministry")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = Ministry
        fields = ['ministry_code', 'ministry_name']


class DutyStationForm(forms.ModelForm):
    duty_station_code = forms.CharField(
        label='Duty Station Code',
        required=True
    )
    duty_station_name = forms.CharField(
        label='Duty Station Name',
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(DutyStationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('duty_station_code', css_class="col-sm-3"),
                    Div('duty_station_name', css_class='col-sm-9'),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("duty-station")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = DutyStation
        fields = ['duty_station_code', 'duty_station_name']


class SectionForm(forms.ModelForm):
    section_code = forms.CharField(
        label='Section Code',
        required=True
    )
    section_name = forms.CharField(
        label='Section Name',
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('section_code', css_class="col-sm-3"),
                    Div('section_name', css_class='col-sm-9'),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("section")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = Section
        fields = ['section_code', 'section_name']


class EmploymentTypeForm(forms.ModelForm):
    employment_type_code = forms.CharField(
        label='Employment Type Code',
        required=True
    )
    employment_type = forms.CharField(
        label='Employment Type',
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(EmploymentTypeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('employment_type_code', css_class="col-sm-3"),
                    Div('employment_type', css_class='col-sm-9'),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("employment_type")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = EmploymentType
        fields = ['employment_type_code', 'employment_type']


class JobGroupForm(forms.ModelForm):
    job_group_code = forms.CharField(
        label='Job Group Code',
        required=True
    )
    job_group = forms.CharField(
        label='Job Group',
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(JobGroupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('job_group_code', css_class="col-sm-3"),
                    Div('job_group', css_class='col-sm-9'),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("job_group")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = JobGroup
        fields = ['job_group_code', 'job_group']


class DirectorateForm(forms.ModelForm):
    directorate_code = forms.CharField(
        label='Directorate Code',
        required=True
    )
    directorate_name = forms.CharField(
        label='Directorate Name',
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(DirectorateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('directorate_code', css_class="col-sm-3"),
                    Div('directorate_name', css_class='col-sm-9'),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("directorate")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = Directorate
        fields = ['directorate_code', 'directorate_name']
