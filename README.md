# Virtual ENV

<https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/>

```terminal
python3 -m pip install --user virtualenv
```

```terminal
python3 -m venv env
```

```terminal
source env/bin/activate
```

```terminal
which python
// should print /env/bin/python basically path to your vrtualenv
```

```terminal
deactivate
````

## Django

```terminal
pip install django
```

```terminal
pip install django
```

```terminal
django-admin startproject projectname
```

> Create another module inside the app (project).

```terminal
python manage.py startapp base
```

> Start development server.

```terminal
python manage.py runserver
```

> Register this newly created app `base` inside your project's man app.

```settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    // Registered app here.
    'base.apps.BaseConfig'
]

```

### Route Registration

> Create a `urls.py` in your modules directory `eg: base`. Add write urls for your module.

```python

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),
]

```

```python

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Home Page')


def room(request):
    return HttpResponse('Room Page')

```

> Now register your module's url to the projects root module and register your url.

```python

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]

```

### Templates

<https://docs.djangoproject.com/en/4.0/topics/templates/>

> Create a `templates` folder in your projects root directory. and create `home.html` and `room.html`. Now register these directory as your templates directory in your root project's `settings.py`.

```python

'DIRS': [
    BASE_DIR / 'templates',
],

```

### Migrations

> Run default migrations.

```terminal
    python manage.py migrate
```

#### Models

> inside base/models.py

```models.py
class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    # participants = models.ManyToManyField
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

#### Create migrations

> Migrations is generated according to the model description that was created on base/models.py

```terminal.
python manage.py makemigrations
```

```terminal
python manage.py migrate
```

### Admin Panel

> Generate authentication to login to the admin panel.

```terminal
python manage.py createsuperuser
```

> Login to the admin panel <https://localhost:8000/admin>

#### Register your model to admin panel

Register your model in `base/admins.py`

```python
from .models import Room

admin.site.register(Room)
```

#### Relation Models (One to many)

> Create a `Message` class in `base/models.py`.

```python
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # SET_DEFAULT
    body = models.TextField()
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
```

> Generate Migrations `python manage.py makemigrations`
> Run the migrations `python manage.py migrate`
> And finally register the newly create models to the admin panel.

```python

```