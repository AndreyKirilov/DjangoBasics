from django.urls import path
from Fruitipedia_app.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard_view, name='dashboard')
]
