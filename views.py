from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .models import Details

# Create your views here.
def index(request):
    det = Details.objects.all()
    sam = {
        'name' : det[0].name,
        'age' : det[0].age,
        'college' :'IES University',
        'course' : 'B-Tech'
    }
    return render(request,'index.html',sam)

def API(request):
    # name = str(request.POST['name'])
    # age = str(request.POST['age'])
    # height = str(request.POST['height'])
    # weight = str(request.POST['weight'])
    # amount_of_word = len(name.split())
    
    # return render(request,'download.html',{'amount':word})
    
    data_sets = []

    # Retrieve details from the Details model
    details_objects = Details.objects.all()

    # Iterate through each detail object and add to the data_sets list
    for detail_object in details_objects:
        data_set = {
            'details':{
            'id':detail_object.id,
            'name': detail_object.name,
            'age': detail_object.age,
            'height': detail_object.height,
            'weight': detail_object.weight}
        }
        data_sets.append(data_set)

    # Return the data_sets list as a JSON response
    return JsonResponse(data_sets, safe=False)