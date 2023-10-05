from django.shortcuts import render


def index(request):
    return render(request, 'push_stud/main.html')
