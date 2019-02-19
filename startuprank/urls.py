from django.urls import path

from . import views

app_name = 'startuprank'

urlpatterns = [
    path('', views.index, name='index'),
    path('allstartups/', views.allstartups, name="allstartups"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('startups/<int:startup_id>/', views.startup, name='startup'),
    path('startups/<int:startup_id>/reviews/', views.reviews, name='reviews'),
    path('startups/<int:startup_id>/reviews/<int:review_id>', views.review, name='review'),
]