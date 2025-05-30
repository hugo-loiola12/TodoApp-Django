# Todo App (Django)

Este é um simples aplicativo de lista de tarefas (TODO) feito com Django.

---

## 💻 Pré-requisitos

- Python 3.8+
- pip
- Windows / macOS / Linux

---

## 🚀 Como executar localmente

1. **Crie e ative o ambiente virtual**

   ```bash
   py -m venv .venv
   # Windows
   .\.venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```

2. **Instale as dependências**

   ```bash
   py -m pip install Django
   ```

3. **Crie o projeto Django**

   ```bash
   django-admin startproject todoApp
   cd todoApp
   ```

4. **Aplique migrações e crie superusuário**

   ```bash
   py manage.py migrate
   py manage.py createsuperuser
   ```

5. **Inicie o servidor**

   ```bash
   py manage.py runserver
   ```

6. **Acesse no navegador**

   - Painel Admin: `http://127.0.0.1:8000/admin/`
   - App TODO: `http://127.0.0.1:8000/`

---

## 📁 Estrutura do Projeto

```
todoApp/
├── todoApp/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todo_list/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── about.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── manage.py
```

---

## ⚙️ Configurações Principais

### `settings.py`

```python
INSTALLED_APPS = [
    # apps Django…
    'todo_list',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],            # usa apenas templates dentro dos apps
        'APP_DIRS': True,      # procura em each_app/templates/
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

---

## 🔗 Rotas (URLs)

### Projeto (`todoApp/urls.py`)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_list.urls')),
]
```

### App (`todo_list/urls.py`)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,  name='home'),
    path('about/', views.about, name='about'),
]
```

---

## 📄 Modelos (Models)

### `todo_list/models.py`

```python
from django.db import models

class Todo(models.Model):
    title        = models.CharField(max_length=200)
    isCompleted  = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

Após criar o model, não esqueça de:

```bash
py manage.py makemigrations
py manage.py migrate
```

E registrar no admin (em `todo_list/admin.py`):

```python
from django.contrib import admin
from .models import Todo

admin.site.register(Todo)
```

---

## 🖥️ Views

### `todo_list/views.py`

```python
from django.shortcuts import render
from .models import Todo

def home(request):
    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'todos': todos})

def about(request):
    return render(request, 'about.html', {})
```

---

## 📑 Templates

### `templates/base.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Todo App</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css"
      rel="stylesheet"
      crossorigin="anonymous"
    />
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="{% url 'home' %}">Todo App</a>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="{% url 'home' %}">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'about' %}">About</a>
          </li>
        </ul>
      </div>
    </nav>
    <div class="container mt-4">{% block content %}{% endblock %}</div>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/js/bootstrap.bundle.min.js"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### `templates/home.html`

```html
{% extends 'base.html' %} {% block content %}
<h1>My Todo List</h1>

<ul class="list-group my-3">
  {% for todo in todos %}
  <li class="list-group-item d-flex justify-content-between align-items-center">
    {{ todo.title }} {% if todo.isCompleted %}
    <span class="badge bg-success">Done</span>
    {% else %}
    <span class="badge bg-secondary">Pending</span>
    {% endif %}
  </li>
  {% empty %}
  <li class="list-group-item">Nenhuma tarefa ainda.</li>
  {% endfor %}
</ul>

<form method="POST">
  {% csrf_token %}
  <div class="input-group">
    <input
      type="text"
      name="title"
      class="form-control"
      placeholder="Nova tarefa..."
      required
    />
    <button class="btn btn-primary">Add</button>
  </div>
</form>
{% endblock %}
```

### `templates/about.html`

```html
{% extends 'base.html' %} {% block content %}
<h1>About</h1>
<p>Este é um simples app de lista de tarefas construído com Django.</p>
{% endblock %}
```

---

## 🎯 Funcionalidades

- Criar / listar tarefas
- Marcar como concluída
- Remover tarefas
- Interface com Bootstrap 5

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
