from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Fruitipedia_app.common.urls')),
    path('fruit/', include('Fruitipedia_app.fruits.urls')),
    path('profile/', include('Fruitipedia_app.profiles.urls'))
]
