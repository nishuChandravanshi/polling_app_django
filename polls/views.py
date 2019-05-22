
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render  #either this or above line

# Create your views here.



def index(request):
    # return HttpResponse("heya! You're at the polls index")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]   #tutorial 3

    # output = ', '.join([q.question_text for q in latest_question_list])
    # -->template = loader.get_template('polls/index.html')

    context={'latest_question_list':latest_question_list,}
    #its like a dictionary with key and value


    # -->return HttpResponse(template.render(context,request))
    # --> (replacing those) with below line using shortcut render()
    return render(request,'polls/index.html',context)
    #theory:The render() function takes the request object as its
    # first argument, a template name as its second argument and a
    # dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.




def detail(request,question_id):
    # return HttpResponse("you're looking at question %s." % question_id)


    # or to generate Http404 error if the requested id isnt present
    # 1st method

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request,'polls.detail.html',{'question':questions})

    # # or 2nd shortcut method
    # import get_object_or_404,render

    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/details.html', {'question':question})



def results(request, question_id):
    response = "you're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("you're voting on question %s."% question_id)
