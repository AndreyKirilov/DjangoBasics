from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from TaskApp.todo_app.forms import SomeForm, NameForm, ContactForm, NewsletterForm, BookFormSet
from TaskApp.todo_app.models import Task, Book
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from TaskApp.todo_app.mixins import SetTimeRestriction


def index(request):

    context = {
        "current_time": datetime.now(),
        "person": {
            "age": 20,
            "height": 190,
        },
        "ids": ["62348764", "fwhj827634", "42y3tyr"],
        "some_text": "Hello",
        "users": [
            "pesho",
            "ivan",
            "stamat",
            "saria",
            "magdalena"
        ]
    }

    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create django project?",
                "author": "Diyan Kalaydzhiev",
                "content": "I **really** don't how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 1?",
                "author": "",
                "content": "### I really don't know how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 2?",
                "author": "Diyan Kalaydzhiev",
                "content": "",
                "created_at": datetime.now(),
            },
        ]
    }

    return render(request, 'posts/dashboard.html', context)


def form_view(request):
    form = SomeForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]

            context = {"username": username,
                       "email": email}

            return render(request, "greeting.html", context)

        else:
            return render(request, 'some_form.html')

    context = {"form": form}
    return render(request, "some_form.html", context)


def name_form_view(request):
    form = NameForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            context = {"name": first_name,
                       "surname": last_name
                       }
            return render(request, "greeting.html", context)

    return render(request, "some_form.html", {"form": form})


def contact_newsletter_view(request):
    contact_form = ContactForm(request.POST or None, prefix='contact')
    newsletter_form = NewsletterForm(request.POST or None, prefix='newsletter')

    if 'contact-username' in request.POST and contact_form.is_valid():
        contact_username = contact_form.cleaned_data['username']
        return render(request, "greeting.html", {'message': f"Thank you {contact_username} for contacting us"})

    elif 'newsletter-email' in request.POST and newsletter_form.is_valid():
        return render(request, 'greeting.html', {"message": 'Thank you for subscribing'})

    return render(request, 'contact_subscribe.html', {'contact_form': contact_form,
                                                                         'newsletter_form': newsletter_form})


def book_view(request):
    formset = BookFormSet(request.POST or None)

    if request.method == "POST" and formset.is_valid():
        author = formset.cleaned_data['author']
        description = formset.cleaned_data['description']

        context = {
            'formset': formset,
            'author': author,
            'description': description
        }

        formset.save()
        return render(request, 'book.html', context=context)

    context = {
        'formset': formset
    }

    return render(request, 'book_form.html', context=context)

# Class based views exercise


class HomePage(SetTimeRestriction, TemplateView):
    template_name = 'home_page.html'


class TaskView(ListView):
    model = Task
    template_name = 'task_display.html'
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Task.objects.filter(name__icontains=query)
        return Task.objects.all()


class CreateTaskView(CreateView):
    model = Task
    fields = ['name', 'description']
    template_name = 'create-instance.html'
    success_url = reverse_lazy('tasks-list')

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        if name[0] != 'A':
            form.add_error('name', "The name should only start with 'A'")
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = "A name for the new task"
        initial['description'] = "A description for the new task"
        return initial


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update_task.html'
    fields = ['description']
    success_url = reverse_lazy('tasks-list')

    def form_valid(self, form):
        created_at = form.cleaned_data.get('created_at')
        if created_at and created_at > datetime.date.today():
            form.add_error('created_at', 'The date cannot be in the future!')
            return self.form_invalid(form)

        return super().form_valid(form)


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('tasks-list')


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_display.html'


class BookCreateView(CreateView):
    model = Book
    fields = ['author', 'description', 'price']
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('books-list')
