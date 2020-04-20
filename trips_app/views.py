from django.shortcuts import render, redirect
from django.http import HttpResponse
from trips_app.models import Trips
from trips_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import logging
from django.template import loader


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
        all_Trips = Trips.objects.filter(owner=request.user)
        paginator = Paginator(all_Trips, 10)
        page = request.GET.get('page')
        all_Trips = paginator.get_page(page)
        return render(request, 'trip.html', {'all_Trips': all_Trips})


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


def map(request):
    payload = requset.body
    print(payload)
    if request.method == 'GET':
        json_data = json.loads(request.body)  # request.raw_post_data w/ Django < 1.4
        try:
            data = json_data['data']
        except KeyError:
            HttpResponseServerError("Malformed data!")
        HttpResponse("Got json data")
    context = {
        'latitude' : 'request.latitude'
    }
    mapbox_access_token = 'pk.my_mapbox_access_token'
    print("--------------"*20, '\n', request.headers)
    print("--------------" * 20, '\n', request)
    return render(request, 'map.html',
                  {'mapbox_access_token': mapbox_access_token},context)
    #return render(request, 'map.html', context)


def about(request):
    context = {
        'about_text': "Welcome from the About Page"
    }
    return render(request, 'about.html', context)


@login_required()
def delete_task(request, task_id):
    task = Trips.objects.get(pk=task_id)
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
        task = Trips.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, "Trip Edited:")
        return redirect('trip')
    else:
        task_obj = Trips.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})
