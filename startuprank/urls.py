from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'startuprank'

urlpatterns = [
    path('', views.index, name='index'),
    path('allstartups/', views.allstartups, name="allstartups"),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('startups/<int:startup_id>/', views.startup, name='startup'),
    path('startups/<int:startup_id>/reviews/', views.reviews, name='reviews'),
    path('startups/<int:startup_id>/add/', views.add, name='add'),
]