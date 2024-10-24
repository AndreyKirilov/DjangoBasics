from django.urls import path
from Fruitipedia_app.profiles import views

urlpatterns = [
    path('create/', views.create_profile_view, name='profile-create'),
    path('details/', views.details_profile_view, name='profile-details'),
    path('edit/', views.edit_profile_view, name='profile-edit'),
    path('delete/', views.delete_profile_view, name='profile-delete'),
]
