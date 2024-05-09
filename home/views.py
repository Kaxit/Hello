from django.shortcuts import render, HttpResponse
from .models import Question
from django.template import loader

divs=[]
for i in range(10):
    divs.append(i)

def game_view2(request):
    question_index = request.session.get('question_index', 0)
    score = request.session.get('score', 0)

    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        correct_answer = Question.objects.get(pk=question_index + 1).answer

        if user_answer.lower() == correct_answer.lower():
            score += 1
        question_index += 1
        request.session['score'] = score
        request.session['question_index'] = question_index

    if question_index < len(Question.objects.all()):
        question = Question.objects.get(pk=question_index + 1).text
    else:
        question = "Game Over. Final Score: {}".format(score)
        # Reset the game if needed
        request.session['question_index'] = 0
        request.session['score'] = 0

    return render(request, 'game/game.html', {'question': question, 'score': score})

# Create your views here.

def index(request):
    # return HttpResponse("This is Home Page")
    return render(request,"index.html")
def Ind_AS_1(request):
    return HttpResponse("This is Ind_AS_1 Page")
def Ind_AS_2(request):
    return render(request,"fr/Ind_AS_2.html")
def Ind_AS_7(request):
    return render(request,"fr/Ind_AS_7.html")
def Ind_AS_19(request):
    return render(request,"fr/Ind_AS_19.html")
def Ind_AS_41(request):
    return render(request,"fr/Ind_AS_41.html")
def Ind_AS_37(request):
    return HttpResponse("This is Ind_AS_37 Page")
def Ind_AS_101(request):
    template = loader.get_template('fr/Ind_AS_101.html')
    context = {
        "divs": divs,
        "surname":"Ranpara"
    }
    return render(request,"fr/Ind_AS_101.html", context)
def Ind_AS_102(request):
    return render(request,"fr/Ind_AS_102.html")
def Ind_AS_113(request):
    return render(request,"fr/Ind_AS_113.html")
def Ind_AS_115(request):
    return render(request,"fr/Ind_AS_115.html")
def skreachpad(request):
    return render(request,"skreachpad.html")
def tools(request):
    variable_list = {
        "tds_form": ["24Q","26Q","27EQ"], 
    }
    return render(request, 'tools.html',variable_list)
def game_view(request):
    return render(request, 'game/game.html')
def game_view2(request):
    return render(request, 'game/game2.html')
def calc(request):
    return render(request, 'calc.html')


# Income Tax Act
def it_basic(request):
    return render(request,"dt/it_basic.html")