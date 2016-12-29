from django.shortcuts import render
from django.http import HttpResponse
from .models import Token
# Create your views here.


def index(request, page_num):
    p = int(page_num)
    most_common_tokens = Token.objects.order_by('-freq')[(p*10)-10:p*10]

    context = {'most_common_tokens': most_common_tokens, 'page': p}
    return render(request, 'annotation/index.html', context)
