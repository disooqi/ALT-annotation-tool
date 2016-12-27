from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    context = {'latest_question_list': [1,2,3,4,5,6]}
    return render(request, 'annotation/index.html', context)