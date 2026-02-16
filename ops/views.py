from django.shortcuts import render, get_list_or_404, redirect
from .models import Service, Incident, PostMortem
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm, IncidentForm, PostMortemForm

# Home
def index(request):
    return render(request, 'ops/index.html')

# lists

def incident_list(request):
    search = request.GET.get('search', '')
    incidents = Incident.objects.all()
    if search:
        incidents = incidents.filter(title__icontains=search)
    else:
        incidents = Incident.objects.all()
    return render(request, 'ops/incidents/incident_list.html', context={'incidents': incidents})

def service_list(request):
    search = request.GET.get('search', '')
    services = Service.objects.all()
    if search:
        services = services.filter(name__icontains=search)
    else:
        services = Service.objects.all()
    return render(request, 'ops/services/service_list.html', context={'services': services})

def postmortem_list(request):
    search = request.GET.get('search', '')
    postmortem = PostMortem.objects.all()
    if search:
        postmortem = postmortem.filter(impact__icontains=search)
    else:
        postmortem = PostMortem.objects.all()
    return render(request, 'ops/postmortem/postmortem_list.html', context={'postmortems': postmortem})


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
