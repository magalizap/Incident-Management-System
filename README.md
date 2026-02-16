# 🛠 Incident Management System

A Django-based web application for managing services, incidents, and post-mortems.
Designed to simulate real-world operational workflows inspired by DevOps and SRE practices.

## 🧰 Tech Stack

- **Python 3.12.7**
- **Django 6.0.2**
- **SQLite** (default development database)
- **Bootstrap** (form styling)
- HTML5 / CSS3

---

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/your-username/incident-management.git

cd incident-management

# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver
```

## 1️⃣ Create a Service

📍 Location:

Services → Create Service

Why first?
Every Incident must be linked to a Service.

## 2️⃣ Create an Incident

📍 Location:

Incidents → Create Incident

Requirements:

Must be logged in.

Must select an existing Service.

## 3️⃣ Change Incident Status to RESOLVED

Before creating a PostMortem, update an incident:

Edit Incident

Set Status = RESOLVED

Optionally set resolved_at

This step is required.

## 4️⃣ Create a Post-Mortem

📍 Location:

PostMortems → Create PostMortem

Business rule:
The Incident dropdown only shows incidents with RESOLVED status.

This filtering is enforced in forms.py using:

```py
self.fields['incident'].queryset = Incident.objects.filter(status='RESOLVED')
```
---
## 🔒 Business Rules

- Only authenticated users can create Incidents, Post-Mortems and Services.
- Post-mortems can only be created for incidents with status `RESOLVED`.
- Cascade deletion:
  - Deleting a Service removes related Incidents.
  - Deleting an Incident removes its PostMortem.
