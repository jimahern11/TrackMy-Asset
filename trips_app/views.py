from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest
from trips_app.models import Trips
from trips_app.models import Locations
from trips_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import logging
from django.template import loader
import json
import requests
from django.http import JsonResponse


logging.basicConfig(filename='views.logs', level=logging.DEBUG)


@login_required()
def trip(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit - False)
            instance.owner = request.user
            instance.save()
        messages.success(request, "New Trip Added:")
        return redirect('trip')
    else:
        all_Trips = Locations.objects.filter(owner=request.user)
        #all_Trips = Trips.objects.filter(owner=request.user)
        paginator = Paginator(all_Trips, 10)
        page = request.GET.get('page')
        all_Trips = paginator.get_page(page)
        return render(request, 'trip.html', {'all_Trips': all_Trips})



def get_trip_data(request):
    url = 'http://localhost:8000/map/'
    r = requests.get(url)
    titles = r.json()
    print('what is in data',titles['data'])


def contact(request):
    context = {
        'contact_text': "Welcome from the Contact Page"
    }
    return render(request, 'contact.html', context)


def index(request):
    context = {
        'index_text': "Welcome from the Index Page"
    }
    return render(request, 'index.html', context)


#def mapJsonData(request):
    #url = 'http://192.168.1.25:22/gps_dashboard.py'
    #response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    #json_string = json.dumps(response)
    #return render(request, 'map.html', {'dataset': json_string})



def save_trips(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)  # request.raw_post_data w/ Django < 1.4
        try:
            data = json_data['data']
        except KeyError:
            HttpResponseServerError("Malformed data!")
        HttpResponse("Got json data")
        return render(request, 'map.html',
                      {'mapbox_access_token': mapbox_access_token}, data)



def map(request):

    latitude = request.GET.get('latitude')
    long = request.GET.get('longitude')
    print('anything here kkkkkkkkkkkkkkkk', latitude)
    print('anything here kkkkkkkkkkkkkkkk', long)
    print("--------------" * 20, '\n')

    gps_data = []
    for key, value in request.GET.items():
        gps_data.append(value)
        gps_data.sort()
        print('The Key is : %s' % (key))
        print('The Value is : %s' % (value))
        print("--------------" * 20, '\n')
        print('What is in the list',gps_data)
        print('What type is gps data :',type(gps_data))
        #print(request.GET.items())

    #print("--------------"*20, '\n', request.headers)
    print('what is in the request attribute',"--------------" * 20, '\n', request)
    person = {'firstname' : 'James','lastname': 'Ahern'}
    gps = [ 52.65897, 123456, 'westbury']

    context = {
        'gps_data': gps_data,
        'person' : person,
        'gps' : gps

    }
    for key, value in context.items():
        print('What is in the value',value)
        print('What is in the key', key)
    print('What type is context',type(context))
    #return render(request, 'map.html', {'gps_data': gps_data })
    return render(request, 'map.html', context)

    #return render(request,'map.html',{'list' : ['hello did this work','if so Ill shoot myself']})



def about(request):
    context = {
        'about_text': "Welcome from the About Page"
    }
    return render(request, 'about.html', context)


@login_required()
def delete_task(request, task_id):
    task = Locations.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else:
        messages.error(request, "Access Restricted, You are not allowed")
    return redirect('trip')


@login_required()
def complete_task(request, task_id):
    task = Trips.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('trip')


@login_required()
def pending_task(request, task_id):
    task = Trips.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, "Access Restricted, You are not allowed")
    return redirect('trip')


@login_required()
def edit_task(request, task_id):
    if request.method == "POST":
        task = Locations.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, "Trip Edited:")
        return redirect('trip')
    else:
        task_obj = Trips.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})
