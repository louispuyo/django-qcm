from django.db import models


class Questionnaire(models.Model):
    titre = models.CharField(max_length=200)

    def __str__(self):
        return self.titre


class Question(models.Model):
    enonce = models.TextField()
    image = models.ImageField(upload_to='uploads/qcm/',
                              verbose_name="Image liée à la question",
                              blank=True)
    questionnaires = models.ManyToManyField(Questionnaire, blank=True)

    def __str__(self):
        return self.enonce


class Reponses(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reponse = models.CharField(max_length=200, blank=True)
    bonne_reponse = models.BooleanField(verbose_name='Bonne réponse.', default=False)
