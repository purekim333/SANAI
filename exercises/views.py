from django.shortcuts import render, redirect

from .models import Exercise
from .forms import ExerciseForm

# Create your views here.
def index(request):
    exercises = Exercise.objects.all()
    context = {
        'exercises' : exercises,
    }
    return render(request, 'exercises/index.html', context)

def detail(request, exercise_pk):
    exercise = Exercise.objects.get(pk=exercise_pk)
    context = {
        'exercise' : exercise,
    }
    return render(request, 'exercises/detail.html', context)

def create(request):
    if request.method == 'POST' :
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save()
            return redirect('exercises:detail', exercise.pk)
    else :
        form = ExerciseForm()
    context = {
        'form' : form,
    }
    return render(request, 'exercises/create.html', context)
            

def delete(request, exercise_pk):
    if request.method == 'POST' :
        exercise = Exercise.objects.get(pk=exercise_pk)
        exercise.delete()
    return redirect('exercises:index')
    

def update(request, exercise_pk):
    exercise = Exercise.objects.get(pk=exercise_pk)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance = exercise)
        if form.is_valid():
            form.save()
            return redirect('exercises:detail', exercise.pk)
    else:
        form = ExerciseForm(instance=exercise)
    context = {
        'form' : form,
        'exercise' : exercise,
    }
    return render(request, 'exercises/update.html', context)

def participate(request, exercise_pk):
    exercise = Exercise.objects.get(pk=exercise_pk)
    me = request.user

    if me in exercise.participators.all() :
        exercise.participators.remove(me)
    else :
        exercise.participators.add(me)
    return redirect('exercises:detail', exercise_pk)