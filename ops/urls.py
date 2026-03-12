from django.urls import path 
from .views import index, IncidentListView, ServiceListView, PostMortemListView, IncidentDetailView, ServiceDetailView, PostMortemDetailView, incident_form, service_form, postmortem_form

app_name = 'ops'

urlpatterns = [
    path('', index, name='index'),
    # lists
    path('incidents/', IncidentListView.as_view(), name='incident_list'),
    path('services/', ServiceListView.as_view(), name='service_list'),
    path('postmortem/', PostMortemListView.as_view(), name='postmortem_list'),

    # details
    path('incidents/<int:pk>/', IncidentDetailView.as_view(), name='incident_detail'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('postmortem/<int:pk>/', PostMortemDetailView.as_view(), name='postmortem_detail'),

    # forms
    path('incidents/form', incident_form, name='incident_form'),
    path('services/form', service_form, name='service_form'),
    path('postmortem/form', postmortem_form, name='postmortem_form')
]