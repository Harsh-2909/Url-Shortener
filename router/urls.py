from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('how-to/', views.how_to, name='how-to'),
    path('<slug:key>/', views.redirector, name='redirector')
]