from django.urls import path
from Fruitipedia_app.fruits import views

urlpatterns = [
    path('create/', views.create_fruit_view, name='fruit-create'),
    path('<int:fruitId>/details/', views.details_fruit_view, name='fruit-details'),
    path('<int:fruitId>/edit/', views.edit_fruit_view, name='fruit-edit'),
    path('<int:fruitId>/delete/', views.delete_fruit_view, name='fruit-delete')
]
