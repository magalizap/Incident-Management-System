from django.shortcuts import render
from .models import Service, Incident, PostMortem
from .forms import ServiceForm, IncidentForm, PostMortemForm
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy

# auth
class CustomLoginView(LoginView):
    template_name = 'ops/auth/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('ops:index')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('ops:login')

class RegisterView(CreateView):
    template_name = 'ops/auth/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('ops:login')

    def form_valid(self, form):
        messages.success(self.request, 'Account created successfully. You can now log in.')
        return super().form_valid(form)
    
# pages
    
class HomeView(TemplateView):
    template_name = 'ops/index.html'

class AboutView(TemplateView):
    template_name = 'ops/components/about.html'


# lists
class IncidentListView(ListView):
    model = Incident
    template_name = 'ops/incidents/incident_list.html'
    context_object_name = 'incidents'

    def get_queryset(self):
        self.queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            self.queryset = self.queryset.filter(title__icontains=search)
        return self.queryset

class ServiceListView(ListView):
    model = Service
    template_name = 'ops/services/service_list.html'
    context_object_name = 'services'

    def get_queryset(self):
        self.queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            self.queryset = self.queryset.filter(name__icontains=search)
        return self.queryset

class PostMortemListView(ListView):
    model = PostMortem
    template_name = 'ops/postmortem/postmortem_list.html'
    context_object_name = 'postmortems'

    def get_queryset(self):
        self.queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            self.queryset = self.queryset.filter(impact__icontains=search)
        return self.queryset


# details

class IncidentDetailView(DetailView):
    model = Incident
    template_name = 'ops/incidents/incident_detail.html'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'ops/services/service_detail.html'

class PostMortemDetailView(DetailView):
    model = PostMortem
    template_name = 'ops/postmortem/postmortem_detail.html'


# update
class IncidentUpdateView(UpdateView):
    model = Incident
    form_class = IncidentForm
    template_name = 'ops/incidents/incident_form.html'
    success_url = reverse_lazy('ops:incident_list')


class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'ops/services/service_form.html'
    success_url = reverse_lazy('ops:service_list')

class PostMortemUpdateView(UpdateView):
    model = PostMortem
    form_class = PostMortemForm
    template_name = 'ops/postmortem/postmortem_form.html'
    success_url = reverse_lazy('ops:postmortem_list')


# delete

class IncidentDeleteView(DeleteView):
    model = Incident
    success_url = reverse_lazy('ops:incident_list')

class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('ops:service_list')

class PostMortemDeleteView(DeleteView):
    model = PostMortem
    success_url = reverse_lazy('ops:postmortem_list')


# forms
class IncidentCreateView(CreateView):
    model = Incident
    form_class = IncidentForm
    template_name = 'ops/incidents/incident_form.html'
    success_url = reverse_lazy('ops:incident_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'ops/services/service_form.html'
    success_url = reverse_lazy('ops:service_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PostMortemCreateView(CreateView):
    model = PostMortem
    form_class = PostMortemForm
    template_name = 'ops/postmortem/postmortem_form.html'
    success_url = reverse_lazy('ops:postmortem_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)