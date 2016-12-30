from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Token, TokenOccurrence
# Create your views here.


def index(request, page_num):
    p = int(page_num)
    most_common_tokens = Token.objects.order_by('-freq')[(p*10)-10:p*10]

    context = {'most_common_tokens': most_common_tokens, 'page': p}
    return render(request, 'annotation/index.html', context)


def detail(request, token_id):
    token = get_object_or_404(Token, pk=token_id)
    #occurrences = token.tweet_set.all()
    tweet_occurPosition_list = list()
    #for tweet in occurrences:
    token_occur_QuerySet = TokenOccurrence.objects.filter(token=token)
    for occur in token_occur_QuerySet:
        tweet_occurPosition_list.append((occur.tweet.tweet_text, occur.position))

    return render(request, 'annotation/detail.html', {'token': token, 'occurrences':tweet_occurPosition_list})


def ambiguous(request, token_id):
    pass

