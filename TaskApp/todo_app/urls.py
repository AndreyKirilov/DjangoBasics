from django.urls import path
from TaskApp.todo_app.views import dashboard, index, form_view, name_form_view, contact_newsletter_view, book_view

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dash'),
    path('my-form/', form_view, name='form'),
    path('name-form/', name_form_view, name='name_form'),
    path('contact-subscribe', contact_newsletter_view, name='contact_subscribe'),
    path('book/', book_view, name='book'),
]
