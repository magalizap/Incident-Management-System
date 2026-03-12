from django.shortcuts import render, get_list_or_404, redirect
from .models import Service, Incident, PostMortem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ServiceForm, IncidentForm, PostMortemForm
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

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

"""@login_required
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
    })"""

class IncidentCreateView(LoginRequiredMixin, CreateView):
    model = Incident
    form_class = IncidentForm
    template_name = 'ops/incidents/incident_form.html'
    success_url = reverse_lazy('ops:incident_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    

"""@login_required
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
    })"""

class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'ops/services/service_form.html'
    success_url = reverse_lazy('ops:service_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    



"""@login_required
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
    })"""

class PostMortemCreateView(LoginRequiredMixin, CreateView):
    model = PostMortem
    form_class = PostMortemForm
    template_name = 'ops/postmortem/postmortem_form.html'
    success_url = reverse_lazy('ops:postmortem_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)