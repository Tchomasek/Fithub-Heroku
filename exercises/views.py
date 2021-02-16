from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .forms import SearchForm
from .models import Exercise, Tag

def home_view(request, *args, **kwargs):    
    return render(request, 'pages/home.html', context = {}, status = 200)

def search_view(request, *args, **kwargs):
    search = request.GET['search']
    return render(request, 'pages/search.html', context = {'search': search}, status = 200)


def ex_list_view(request, *args, **kwargs):
    qs = Exercise.objects.all()
    ex_list = [x.serialize() for x in qs]
    data = {
        'is_user': False,
        'response': ex_list
    }
    return JsonResponse(data)

def ex_detail_view(request, ex_id, *args, **kwargs):
    data = {
        'id': ex_id,
    }
    status = 200
    try:
        obj = Exercise.objects.get(id=ex_id)
        data['name'] = obj.name
        data['description'] = obj.description
        data['link'] = str(obj.link)
    except:
        data['message'] = 'not found'
        status = 404
    return render(request, 'exercises/detail.html', context = data, status = 200)
    #return JsonResponse(data, status = status)