from django.http import HttpResponse
from .models import Startup, Review
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

def index(request):
    return render(request, 'startuprank/index.html', {})

def allstartups(request):
    latest_startups_established = Startup.objects.order_by('-estab_year', 'title')[:10]
    context = {'latest_startups_established': latest_startups_established}
    return render(request, 'startuprank/allstartups.html', context)

def startup(request, startup_id):
    startup = get_object_or_404(Startup, pk=startup_id)
    return render(request, 'startuprank/startup.html', {'startup': startup})

def reviews(request, startup_id):
    startup_reviews = Review.objects.filter(startup_id=startup_id)
    return render(request, 'startuprank/reviews.html',
        {'startup_reviews': startup_reviews })

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def add(request, startup_id):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        review_date = timezone.now()
        startup_id = startup_id

        add = Review(startup_id=startup_id, title=title, text=text, review_date=review_date)
        add.save()

        return HttpResponseRedirect(reverse('startuprank:reviews', args=(startup_id,)))
    else:
        return render(request, 'add.html')

