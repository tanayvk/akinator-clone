from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Question, Person, Response

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def start(request):
    request.session['possible'] = Person.all()
    return HttpResponseRedirect(reverse('question', args=(1,)))

def question(request, question_id):
    ques = False
    if 1 <= question_id <= Question.objects.count():
        ques = Question.objects.get(id=question_id)
    context = {
        'question': ques,
    }
    return render(request, 'main/question.html', context)

def question_submit(request, question_id):
    ques = Question.objects.get(id=question_id)
    choice = request.POST['choice'] == "1"

    current = Response.get_people(ques, (choice == ques.default) ^ choice)
    if choice == ques.default:
        current = list(set(Person.all()).difference(set(current)))

    possible = request.session.get('possible', Person.all())
    possible = list(set(possible).intersection(set(current)))
    request.session['possible'] = possible
    if len(possible) == 1 or len(possible) == 0 or question_id == Question.objects.count():
        return HttpResponseRedirect(reverse('result'))
    return HttpResponseRedirect(reverse('question', args=(question_id + 1,)))

def result(request):
    context = {
        'possible': request.session.get('possible', [])
    }
    return render(request, 'main/result.html', context)
