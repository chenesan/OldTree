# -*- coding: utf-8 -*-
import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import MessageForm, QuestionsForm
from .models import Tree, Message

def index(request):
    return render(request, 'index.html', {})

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
            his_trees = Tree.objects.filter(division='中正區')
            his_tree = his_trees[random.randint(0, len(his_trees) - 1)]
            return render(request, 'your_tree.html', {
                'gender': data['gender'],
                'tree': his_tree,
            })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionsForm()
    return render(request, 'questions.html', {'form': form})

def your_tree(request):
    return render(request, 'your_tree.html', )

def message(request):
    return render(request, 'message.html', {
        'messages': Message.objects.all()
    })

def send_message(request):
    if request.POST:
        data = request.POST
        form = MessageForm(data)
        if form.is_valid():
            Message.objects.create(content=data['content'])
            return JsonResponse({})
    return JsonResponse({})
