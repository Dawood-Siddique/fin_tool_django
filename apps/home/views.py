from django.shortcuts import render
from django.views import View
from .models import EUModel
from random import randint
from django.forms.models import model_to_dict
from django.http import JsonResponse

# Create your views here.

class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')

class RandomChartData(View):
    def get(self, request):
        window = 100
        index = randint(0, EUModel.objects.count() - window)
        chart = EUModel.objects.filter(id__range=(index, index + window))
        data = [model_to_dict(obj) for obj in chart]
        return JsonResponse(data, safe=False)