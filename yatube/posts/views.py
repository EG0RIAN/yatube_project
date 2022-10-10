from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    template = 'posts/index.html'
    main_text = 'Это главная страница проекта Yatube'
    context = {
        'main_text': main_text
    }
    return render(request, template, context) 

def group_posts(request, pk):
    template = 'posts/group_list.html'
    main_text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'main_text': main_text
    }
    return render(request, template, context)