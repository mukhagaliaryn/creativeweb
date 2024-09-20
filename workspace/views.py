from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Home page
@login_required(login_url='/accounts/login/')
def home_view(request):
    context = {
        'numbers': range(1, 5)
    }
    return render(request, 'index.html', context)


# Lessons page
def lessons_view(request):

    return render(request, 'lessons/index.html', {})
