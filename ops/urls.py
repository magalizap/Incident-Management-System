from django.urls import path 
from .views import index, service_list, incident_list, postmortem_list, incident_form, service_form, postmortem_form

app_name = 'ops'

urlpatterns = [
    path('', index, name='index'),
    # lists
    path('incidents/', incident_list, name='incident_list'),
    path('services/', service_list, name='service_list'),
    path('postmortem/', postmortem_list, name='postmortem_list'),
    # forms
    path('incidents/form', incident_form, name='incident_form'),
    path('services/form', service_form, name='service_form'),
    path('postmortem/form', postmortem_form, name='postmortem_form')
]