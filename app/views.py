from django.shortcuts import render, redirect
from .forms import QuestionsForm

def index(request):
    return render(request, 'index.html', {})

def start(request):
    return render(request, 'questions.html', {})

def answer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        data = request.POST
        # create a form instance and populate it with data from the request:
        form = QuestionsForm(data)
        # check whether it's valid:
        if form.is_valid():
            return render(request, 'your_tree.html', {
                'gender': data['gender'],
            })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionsForm()

    return render(request, 'questions.html', {'form': form})

def your_tree(request):
    return render(request, 'your_tree.html', )
