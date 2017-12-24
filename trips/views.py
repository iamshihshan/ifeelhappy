# trips/views.py

from datetime import datetime
from django.shortcuts import render
from .forms import NameForm

def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })

def hello_world_name(request, text=None):
    return render(request, 'hello_world_name.html',{
        'endofpath' : text,
        'name': request.GET['name'],
    })

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
