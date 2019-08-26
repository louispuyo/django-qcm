from django.conf.urls import url

from . import views

app_name = "qcm"
urlpatterns = [
    # ex: /qcm/
    url('^$', views.IndexView.as_view(), name='index'),
    url('^questionnaires$', views.QuestionnairesIndexView.as_view(), name='questionnaires_index'),
#    path('detail/<int:question_id>', views.detail, name='detail'),
    url(r'^detail/(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^questionnaires/(?P<questionnaire_id>\d+)/$', views.questionnaire_view, name='detail_questionnaire'),
]
