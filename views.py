from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User ,auth
from django.contrib import messages
import json
from .models import Details

# Create your views here.
def index(request):
    # det = Details.objects.all()
    # sam = {
    #     'name' : det[0].name,
    #     'age' : det[0].age,
    #     'college' :'IES University',
    #     'course' : 'B-Tech'
    # }
    return render(request,'index.html')

def API(request):
    if request.method=='POST':
        name = str(request.POST['name'])
        photo = str(request.POST['link'])
        age = str(request.POST['age'])
        height = str(request.POST['height'])
        weight = str(request.POST['weight'])
        amount_of_word = len(name.split())
        
        user = Details.objects.create(name= name,photo = photo, age = age,height=height,weight = weight)
        user.save()
    # return render(request,'download.html',{'amount':word})
    return redirect('index')


def api(request):
    data_sets = []
    # Retrieve details from the Details model
    details_objects = Details.objects.all()
    # Iterate through each detail object and add to the data_sets list
    for detail_object in details_objects:
        data_set = {
            'id':detail_object.id,
            'photo': detail_object.photo,
            'name': detail_object.name,
            'age': detail_object.age,
            'height': detail_object.height,
            'weight': detail_object.weight
            }
        data_sets.append(data_set)
    # Return the data_sets list as a JSON response
    if data_sets is None:
        return redirect('/')
    else:
        return JsonResponse(data_sets, safe=False)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email is already Register')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username is already Used')
                return redirect('register')
            else :
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('index')
        else:
            messages.info(request,'Password is not Matched')
            return redirect('register')            
    else:   
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        stored_hash = "2ye8UY**************************************"
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Information is not correct')
            return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request,pk):
    # if User.is_authenticated:
    #     pk = User
    return render(request,'profile.html',{'pk':pk})