from django.urls import path
from TaskApp.todo_app.views import (dashboard, HomePage, form_view, name_form_view, contact_newsletter_view, book_view,
                                    TaskView, CreateTaskView, TaskUpdateView, DeleteTaskView, BookListView, BookCreateView)

urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
    path('dashboard/', dashboard, name='dash'),
    path('my-form/', form_view, name='form'),
    path('name-form/', name_form_view, name='name_form'),
    path('contact-subscribe', contact_newsletter_view, name='contact_subscribe'),
    path('book_app/', book_view, name='book_app'),
    path('tasks-list/', TaskView.as_view(), name='tasks-list'),
    path('create-task/', CreateTaskView.as_view(), name='create-task'),
    path('update-task/<int:pk>/', TaskUpdateView.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', DeleteTaskView.as_view(), name='delete-task'),
    path('books-list/', BookListView.as_view(), name='books-list'),
    path('add-book/', BookCreateView.as_view(), name='create-book')
]
