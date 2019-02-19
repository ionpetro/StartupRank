from django.http import HttpResponse
from .models import Startup, Review
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

def index(request):
    latest_startups_established = Startup.objects.order_by('-estab_year', 'title')[:10]
    context = {'latest_startups_established': latest_startups_established}
    return render(request, 'startuprank/index.html', context)

def about(request):
    return render(request, 'startuprank/about.html', {})

def contact(request):
    return render(request, 'startuprank/contact.html', {})

def startup(request, startup_id):
    startup = get_object_or_404(Startup, pk=startup_id)
    return render(request, 'startuprank/startup.html', {'startup': startup})

def reviews(request, startup_id):
    startup_reviews = Review.objects.filter(startup_id=startup_id)
    return render(request, 'startuprank/reviews.html',
        {'startup_reviews': startup_reviews })

#form
def review(request, startup_id, review_id=None):

    if review_id is not None:
        review = get_object_or_404(Review, pk=review_id)
    else:
        review = Review()
        review.startup_id = startup_id

    if request.method == 'POST':
        review.title = request.POST['title']
        review.text = request.POST['text']
        review.review_date = timezone.now()
        review.save()
        return HttpResponseRedirect(reverse('startuprank:reviews', args=(startup_id,)))
    else:
        context = {
        'startup_id': startup_id,
        'review_id': review_id,
        'title': review.title,
        'text': review.text
    }

    return render(request, 'startuprank/review.html', context)

def vote(request, startup_id):
    votes = Vote.objects.all()
    return render(request, 'startupranks/startup.html', {'votes':votes})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
