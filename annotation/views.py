from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Token, Tweet, TokenOccurrence
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


def ambiguous(request):
    ambiguous_tokens = Token.objects.filter(ambiguous=True)
    context = {'ambiguous_tokens': ambiguous_tokens}
    return render(request, 'annotation/ambiguous.html', context)


def ambiguous_detail(request, token_id):
    token = get_object_or_404(Token, pk=token_id)
    tweet_occurPosition_list = list()
    token_occur_QuerySet = TokenOccurrence.objects.filter(token=token)
    for occur in token_occur_QuerySet:
        tweet_occurPosition_list.append((occur.tweet, occur.position, occur.id))
    return render(request, 'annotation/ambiguous_detail.html', {'token': token, 'occurrences':tweet_occurPosition_list})


def occurrence(request, occur_id):
    #token = get_object_or_404(Token, pk=token_id)
    #tweet = get_object_or_404(Tweet, pk=tweet_id)
    occur = get_object_or_404(TokenOccurrence, pk=occur_id)

    context = {'occurrence': occur}
    return render(request, 'annotation/occur_update.html',context)