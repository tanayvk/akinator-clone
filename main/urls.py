from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('question/<int:question_id>/submit', views.question_submit, name='submit-question'),
    path('result/', views.result, name='result'),
]
