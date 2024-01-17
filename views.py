from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json

# Create your views here.
def index(request):

    sam = {
        'name' : 'Sam',
        'age' : 20,
        'college' :'IES University',
        'course' : 'B-Tech'
    }
    return render(request,'index.html',sam)

def API(request):
    name = str(request.GET['name'])
    age = str(request.GET['age'])
    height = str(request.GET['height'])
    weight = str(request.GET['weight'])
    amount_of_word = len(name.split())
    # return render(request,'download.html',{'amount':word})
    data_set = {'words': name, 'amount': str(amount_of_word),'age': age ,'height': height, 'weight': weight}
    return JsonResponse(data_set)