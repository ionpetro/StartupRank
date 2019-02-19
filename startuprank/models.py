from django.db import models
from django.utils import timezone
from vote.models import VoteModel



class Startup(models.Model):
    title = models.CharField(max_length=200)
    estab_year = models.IntegerField('year established', default=2000)
    votes = models.IntegerField(default=0)

    #method that finds the startups that were established the last year
    def was_established_recently(self):
        return (self.estab_year >= timezone.now().year - 1)

    #method that shows at my database shell, which element is which
    def __str__(self):
        return "%s, %s" % (self.title, self.estab_year)

class Review(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(default="")
    review_date = models.DateTimeField('review date')

    #method that shows at my database shell, which element is which
    def __str__(self):
        return "%s, %s, %s" % (self.title, self.text, self.review_date)
