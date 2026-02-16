from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner_team = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Incident(models.Model):

    SEVERITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('INVESTIGATING', 'Investigating'),
        ('RESOLVED', 'Resolved'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='incidents')
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class PostMortem(models.Model):
    incident = models.OneToOneField(Incident, on_delete=models.CASCADE, related_name='postmortem')
    root_cause = models.TextField()
    impact = models.TextField()
    corrective_actions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"PostMortem - {self.incident.title}"
