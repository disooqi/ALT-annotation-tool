# -*- coding:utf-8 -*-
import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Token, Tweet, TokenOccurrence
from .forms import TokenForm, TokenOccurrenceForm

# Create your views here.
pos_tagset = [u'ترقيم', u'عدد', u'أجنبي', u'اسم', u'فعل', u'صفة', u'أداة', u'جر', u'ضمير', u'تعريف', u'عطف', u'لاحق',
              u'اختصار', u'رابط', u'شعور', u'وسم', u'مرجع']


def index(request, page_num):
    p = int(page_num)
    most_common_tokens = Token.objects.order_by('-freq')[(p * 10) - 10:p * 10]

    context = {'most_common_tokens': most_common_tokens, 'page': p}
    return render(request, 'annotation/index.html', context)


def detail(request, token_id):
    token = get_object_or_404(Token, pk=token_id)
    # occurrences = token.tweet_set.all()
    tweet_occurPosition_list = list()
    # for tweet in occurrences:
    token_occur_QuerySet = TokenOccurrence.objects.filter(token=token)
    for occur in token_occur_QuerySet:
        tweet_occurPosition_list.append((occur.tweet.tweet_text, occur.position))

    if request.method == 'POST':
        form = TokenForm(request.POST, instance=token)
        if form.is_valid():
            form.save()
            return render(request, 'annotation/detail.html', {'token': token, 'occurrences': tweet_occurPosition_list})
    else:
        form = TokenForm(instance=token)

    return render(request, 'annotation/detail.html',
                  {'token': token, 'occurrences': tweet_occurPosition_list, 'form': form})


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
    return render(request, 'annotation/ambiguous_detail.html',
                  {'token': token, 'occurrences': tweet_occurPosition_list})


def occurrence(request, occur_id):
    occur = get_object_or_404(TokenOccurrence, pk=occur_id)

    if request.method == 'POST':
        form = TokenOccurrenceForm(request.POST, instance=occur)
        if form.is_valid():
            form.save()
            tweet_occurPosition_list = list()
            token_occur_QuerySet = TokenOccurrence.objects.filter(token=occur.token)
            for occur in token_occur_QuerySet:
                tweet_occurPosition_list.append((occur.tweet, occur.position, occur.id))
            return render(request, 'annotation/ambiguous_detail.html',
                          {'token': occur.token, 'occurrences': tweet_occurPosition_list, 'saved': True})
    else:
        form = TokenOccurrenceForm(instance=occur)

    context = {'occurrence': occur, 'form': form}
    return render(request, 'annotation/occur_update.html', context)


def autocomplete_pos(request, text_value):

    tags = text_value.strip().split('+')
    hints = list()
    suggestions = list()
    for tag in tags[:-1]:
        tag = tag.strip()
        if tag not in pos_tagset:
            hints.append(u'إن الوسم %s غير موجود ضمن القائمة المسموح بإستخدامها' % tag)
    else:
        if tags[-1] not in pos_tagset:
            for pos_tag in pos_tagset:
                if pos_tag.startswith(tags[-1]):
                    suggestions.append(pos_tag)
            else:
                if not suggestions:
                    hints.append(u'إن الوسم %s غير موجود ضمن القائمة المسموح بإستخدامها' % tags[-1])

    print

    return render(request, 'annotation/suggestions.html', {'suggestions':json.dumps(suggestions)})




def tagset(request):
    return render(request, 'annotation/tagset.html')
