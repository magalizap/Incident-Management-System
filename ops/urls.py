from django.urls import path 
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'ops'

urlpatterns = [
    # Home
    path('', login_required(views.HomeView.as_view()), name='index'),
    path('about/', login_required(views.AboutView.as_view()), name='about'),

    # auth
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    # lists
    path('incidents/', login_required(views.IncidentListView.as_view()), name='incident_list'),
    path('services/', login_required(views.ServiceListView.as_view()), name='service_list'),
    path('postmortem/', login_required(views.PostMortemListView.as_view()), name='postmortem_list'),

    # details
    path('incidents/details/<int:pk>', login_required(views.IncidentDetailView.as_view()), name='incident_detail'),
    path('services/details/<int:pk>', login_required(views.ServiceDetailView.as_view()), name='service_detail'),
    path('postmortem/details/<int:pk>', login_required(views.PostMortemDetailView.as_view()), name='postmortem_detail'),

    # update
    path('incidents/update/<int:pk>', login_required(views.IncidentUpdateView.as_view()), name='incident_update'),
    path('services/update/<int:pk>', login_required(views.ServiceUpdateView.as_view()), name='service_update'),
    path('postmortem/update/<int:pk>', login_required(views.PostMortemUpdateView.as_view()), name='postmortem_update'),

    # delete
    path('incidents/delete/<int:pk>', login_required(views.IncidentDeleteView.as_view()), name='incident_delete'),
    path('services/delete/<int:pk>', login_required(views.ServiceDeleteView.as_view()), name='service_delete'),
    path('postmortem/delete/<int:pk>', login_required(views.PostMortemDeleteView.as_view()), name='postmortem_delete'),

    # forms
    path('incidents/form', login_required(views.IncidentCreateView.as_view()), name='incident_form'),
    path('services/form', login_required(views.ServiceCreateView.as_view()), name='service_form'),
    path('postmortem/form', login_required(views.PostMortemCreateView.as_view()), name='postmortem_form')
]