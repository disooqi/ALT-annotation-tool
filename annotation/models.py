from django.db import models

# Create your models here.


class Token(models.Model):
    token_text = models.CharField(max_length=15)
    default_coda = models.CharField(max_length=15, null=True, blank=True)
    default_segmentation = models.CharField(max_length=15, null=True, blank=True)
    default_pos = models.CharField(max_length=15, null=True, blank=True)
    ambiguous = models.BooleanField(default=False)
    freq = models.IntegerField()

    def __unicode__(self):              # __unicode__ on Python 2
        return self.token_text


class Tweet(models.Model):
    tweet_id = models.IntegerField(primary_key=True)
    tweet_text = models.CharField(max_length=140)
    members = models.ManyToManyField(Token, through='TokenOccurrence')

    def __unicode__(self):              # __unicode__ on Python 2
        return self.tweet_text


class TokenOccurrence(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(null=False)
    coda = models.CharField(max_length=15,null=True, blank=True)
    segmentation = models.CharField(max_length=15,null=True, blank=True)
    pos = models.CharField(max_length=15,null=True, blank=True)
