"""
Views are responsible for processing user requests, 
fetching data from the database (if necessary), 
and rendering the appropriate response, 
which could be an HTML page, JSON data, or any other format.

"""


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import RandomQuestionSerializer


class RandomQuestion(APIView):
    def get(self, request, formate=None, **kwargs):
        question = Question.objects.filter().order_by("?")[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)
