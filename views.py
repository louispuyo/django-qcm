from builtins import print

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic
from .models import Question, Reponses, Questionnaire


class IndexView(generic.ListView):
    template_name = 'qcm/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()


class QuestionnairesIndexView(generic.ListView):
    template_name = 'qcm/index_questionnaires.html'
    context_object_name = 'questionnaire_list'

    def get_queryset(self):
        return Questionnaire.objects.all()


def questionnaire_view(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    questions = Question.objects.filter(questionnaires=questionnaire_id)
    # Utilisation d'une session pour stocker le questionnaire en cours.
    request.session['questionnaire_en_cours'] = questionnaire_id
    context = {'questions': questions, 'questionnaire': questionnaire}
    return render(request, 'qcm/detail_questionnaire.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    reponses = Reponses.objects.filter(question_id=question_id)
    context = {'question': question, 'reponses': reponses}
    if request.method == 'POST':
        reponse_brute = request.POST.dict()
        reponses_utilisateur = [key for key, val in reponse_brute.items() if val == 'on']
        # QuerySet pour affihcer en vert les bonnes réponses
        vert = reponses.filter(bonne_reponse=True)
        # list est une table qui contient les queryset dont la réponse est fausse et que l'utilisateur a choisi
        list = []
        for key in reponses_utilisateur:
            list.append(reponses.filter(pk=key).filter(bonne_reponse=False))
        # Rouge est un queryset (et pas une liste) dont la réponse est fausse et que l'utilisateur a choisi
        rouge = Reponses.objects.none()
        for elem in list:
            if bool(elem):
                rouge = rouge | elem
        neutre = reponses.difference(rouge, vert)
        context['vert'] = vert
        context['rouge'] = rouge
        context['neutre'] = neutre
        context['questionnaire_en_cours'] = request.session['questionnaire_en_cours']
        return render(request, 'qcm/reponse.html', context)
    else:
        context['questionnaire_en_cours'] = request.session['questionnaire_en_cours']
        return render(request, 'qcm/detail_question.html', context)
