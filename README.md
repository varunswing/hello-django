# hello-django

Getting started with django REST.

## Prequisites

1. Install Python

## Getting started

```bash
# Step - 1 : Create virtual environment in root project folder
python -m venv myvenv

# Step - 2 : Activate virtual environment (in windows)
myvenv\Scripts\activate
```

## Step - 3

- In root folder create `requirements.txt`

```markdown
Django
```

- Run

```bash
pip install -r requirements.txt
```

## Step - 4

Create first django project

```bash
# In project root directory
django-admin startproject django_api
cd django_api && python manage.py startapp api
```

## Step - 5

Create `/api/urls.py`

```py

```

## Step - 6

Modify `/django_api/urls.py`

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

## References

1. [Django Installation](https://tutorial.djangogirls.org/en/django_installation/)
