# -*- coding: utf-8 -*-
import random
import time
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import MessageForm, QuestionsForm
from .models import Tree, Message

def index(request):
    return render(request, 'index.html', {})

def first_questions(request):
    return render(request, 'first_questions.html', {})

def questions(request):
    return render(request, 'questions.html', {})

def answer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        data = request.POST
        # create a form instance and populate it with data from the request:
        form = QuestionsForm(data)
        # check whether it's valid:
        if form.is_valid():
            his_trees = Tree.objects.filter(division=data['division'])
            his_tree = his_trees[random.randint(0, len(his_trees) - 1)]
            return render(request, 'tree.html', {
                'tree': his_tree,
            })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionsForm()
    return render(request, 'questions.html', {'form': form})

def your_tree(request):
    return render(request, 'tree.html', )

def message(request):
    start = random.randint(0, Message.objects.count() - 2)
    return render(request, 'message.html', {
        'messages': Message.objects.filter(
            id__gte=start,
            id__lte=start + 2,
        )
    })

def send_message(request):
    if request.POST:
        data = request.POST
        form = MessageForm(data)
        if form.is_valid():
            Message.objects.create(content=data['content'])
            return JsonResponse({})
    return JsonResponse({})
