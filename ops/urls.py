from django.urls import path 
from . import views

app_name = 'ops'

urlpatterns = [
    path('', views.index, name='index'),
    # lists
    path('incidents/', views.IncidentListView.as_view(), name='incident_list'),
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('postmortem/', views.PostMortemListView.as_view(), name='postmortem_list'),

    # details
    path('incidents/details/<int:pk>', views.IncidentDetailView.as_view(), name='incident_detail'),
    path('services/details/<int:pk>', views.ServiceDetailView.as_view(), name='service_detail'),
    path('postmortem/details/<int:pk>', views.PostMortemDetailView.as_view(), name='postmortem_detail'),

    # update
    path('incidents/update/<int:pk>', views.IncidentUpdateView.as_view(), name='incident_update'),
    path('services/update/<int:pk>', views.ServiceUpdateView.as_view(), name='service_update'),
    path('postmortem/update/<int:pk>', views.PostMortemUpdateView.as_view(), name='postmortem_update'),

    # delete
    path('incidents/delete/<int:pk>', views.IncidentDeleteView.as_view(), name='incident_delete'),
    path('services/delete/<int:pk>', views.ServiceDeleteView.as_view(), name='service_delete'),
    path('postmortem/delete/<int:pk>', views.PostMortemDeleteView.as_view(), name='postmortem_delete'),

    # forms
    #path('incidents/form', incident_form, name='incident_form'),
    #path('services/form', service_form, name='service_form'),
    #path('postmortem/form', postmortem_form, name='postmortem_form')
    path('incidents/form', views.IncidentCreateView.as_view(), name='incident_form'),
    path('services/form', views.ServiceCreateView.as_view(), name='service_form'),
    path('postmortem/form', views.PostMortemCreateView.as_view(), name='postmortem_form')
]