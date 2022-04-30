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
