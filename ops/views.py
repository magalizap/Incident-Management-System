from django.shortcuts import render, get_list_or_404, redirect
from .models import Service, Incident, PostMortem
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm, IncidentForm, PostMortemForm
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

# Home
def index(request):
    return render(request, 'ops/index.html')

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



# forms

@login_required
def incident_form(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.autor = request.user
            incident.save()
            return redirect('ops:incident_list')
    else:
        form = IncidentForm()

    return render(request, 'ops/incidents/incident_form.html', {
        'incidentForm': form
    })
    

@login_required
def service_form(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.autor = request.user
            service.save()
            return redirect('ops:service_list')
    else:
        form = ServiceForm()

    return render(request, 'ops/services/service_form.html', {
        'serviceForm': form
    })

@login_required
def postmortem_form(request):
    if request.method == 'POST':
        form = PostMortemForm(request.POST)
        if form.is_valid():
            postmortem = form.save(commit=False)
            postmortem.autor = request.user
            postmortem.save()
            return redirect('ops:postmortem_list')
    else:
        form = PostMortemForm()
    
    return render(request, 'ops/postmortem/postmortem_form.html', {
        'postMortemForm': form
    })
