from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]
