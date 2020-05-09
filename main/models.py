from django.db import models

# Create your models here.

class Question(models.Model):
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    default = models.BooleanField()

class Person(models.Model):
    def __str__(self):
        return self.name
    
    def all():
        return list(map(lambda x: str(x.name), list(Person.objects.all())))
    
    name = models.CharField(max_length=100)

class Response(models.Model):
    def __str__(self):
        return "(" + str(self.question) + ", " + str(self.person) + "): " + str(self.value)
    
    def get_people(question, choice):
        responses = list(Response.objects.filter(question=question, value=choice))
        return list(map(lambda x: str(x.person), responses))

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    value = models.BooleanField()

