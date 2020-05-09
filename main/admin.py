from django.contrib import admin

from .models import Question, Person, Response

# Register your models here.
admin.site.register(Question)
admin.site.register(Person)
admin.site.register(Response)
