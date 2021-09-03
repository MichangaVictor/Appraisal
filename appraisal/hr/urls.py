
from django.urls import path, include
from .views import (
                    employee_view, employee_create_view, EmployeeUpdateView, EmployeeDeleteView,
                    designation_view, designation_create_view, DesignationUpdateView, DesignationDeleteView,
                    ministry_view, ministry_create_view, MinistryUpdateView, MinistryDeleteView,
                    station_view, station_create_view, StationUpdateView, StationDeleteView,
                    section_view, section_create_view, SectionUpdateView, SectionDeleteView,
                    employmentType_view, employmentType_create_view, EmploymentTypeUpdateView, EmploymentTypeDeleteView,
                    jobGroup_view, jobGroup_create_view, JobGroupUpdateView, JobGroupDeleteView,
                    directorate_view, directorate_create_view, DirectorateUpdateView, DirectorateDeleteView,

                    )

urlpatterns=[

    #Employee urls
    path('employee/', employee_view, name="employee"),
    path('employee-create/',employee_create_view, name = 'employee-create'),
    path('employee/<pk>/employee-update/', EmployeeUpdateView.as_view(), name = 'employee-update'),
    path('employee/<pk>/employee-delete/',EmployeeDeleteView.as_view(), name = 'employee-delete'),

    #Designation urls
    path('designation/', designation_view, name="designation"),
    path('department_create/',designation_create_view, name = 'department_create'),
    path('designation/<pk>/designation-update/', DesignationUpdateView.as_view(), name = 'designation-update'),
    path('designation/<pk>/designation-delete/', DesignationDeleteView.as_view(), name = 'designation-delete'),

    #Ministry urls
    path('ministry/', ministry_view, name="ministry"),
    path('ministry_create/',ministry_create_view, name = 'ministry_create'),
    path('ministry/<pk>/ministry-update/', MinistryUpdateView.as_view(), name = 'ministry-update'),
    path('ministry/<pk>/ministry-delete/', MinistryDeleteView.as_view(), name = 'ministry-delete'),

    #Duty Stations urls
    path('duty-station/', station_view, name="duty-station"),
    path('station_create/',station_create_view, name = 'station_create'),
    path('duty-station/<pk>/station-update/', StationUpdateView.as_view(), name = 'station-update'),
    path('duty-station/<pk>/station-delete/', StationDeleteView.as_view(), name = 'station-delete'),

    #Sections urls
    path('section/', section_view, name="section"),
    path('section-create/',section_create_view, name = 'section-create'),
    path('section/<pk>/section-update/', SectionUpdateView.as_view(), name = 'section-update'),
    path('section/<pk>/section-delete/', SectionDeleteView.as_view(), name = 'section-delete'),

    #EmploymentType urls
    path('employment_type/', employmentType_view, name="employment_type"),
    path('employment-type-create/',employmentType_create_view, name = 'employment-type-create'),
    path('employment_Type/<pk>/employment-type-update/', EmploymentTypeUpdateView.as_view(), name = 'employment-type-update'),
    path('employment_Type/<pk>/employment-type-delete/', EmploymentTypeDeleteView.as_view(), name = 'employment-type-delete'),

    #Job Groups urls
    path('job_group/', jobGroup_view, name="job_group"),
    path('job-group-create/',jobGroup_create_view, name = 'job-group-create'),
    path('job-group/<pk>/job-group-update/', JobGroupUpdateView.as_view(), name = 'job-group-update'),
    path('job-group/<pk>/job-group-delete/', JobGroupDeleteView.as_view(), name = 'job-group-delete'),

    #Directorate urls
    path('directorate/', directorate_view, name="directorate"),
    path('directorate-create/',directorate_create_view, name = 'directorate-create'),
    path('directorate/<pk>/directorate-update/', DirectorateUpdateView.as_view(), name = 'directorate-update'),
    path('directorate/<pk>/directorate-delete/', DirectorateDeleteView.as_view(), name = 'directorate-delete'),

]