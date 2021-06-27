import os

from django.http import HttpResponse, response, Http404, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import path

from app.forms import BookForm
from app.models import Book
from django.contrib.postgres.search import SearchVector


def search(request):
    lo = request.GET['sea']
    count = Book.objects.all().count()
    god = Book.objects.annotate(search=SearchVector('college', 'department', 'topic', 'subject')).filter(search=lo)
    counts = god.count()
    return render(request, 'result.html', {'god': god, 'count': count, 'cou': counts})


def index(request):
    return render(request, 'index.html')


def upload(request):
    return render(request, 'upload.html')


def download(request):
        contex = Book.objects.all()
        return render(request, 'download.html', {'books': contex})


def create_book(request):
    from django.contrib import messages

    if request.method == 'GET':
        context = {'form': BookForm()}
        messages.info(request, "Please fill the form ....")
        return render(request, 'upload.html', context)

    elif request.method == 'POST':

        # Passing uploaded files as request.files
        form = BookForm(request.POST, request.FILES)

        # Validating and saving the form
        if form.is_valid():

            form.save()
            messages.success(request, "Files saved successfully")
            return redirect('create_book')
        else:
            context = {'form': form}
            messages.warning(request, " Please Try again ....")
            return render(request, 'upload.html', context)


def contact(request):
    return HttpResponse('<h3 style="color:lime">We will update it soon stay tuned</h1>')


def report(request):
    return render(request, 'report.html')


def about(request):
    return render(request, 'about.html')