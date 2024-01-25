from django.shortcuts import render

from blog.models import Menu, Team


# Create your views here.
def index(request):
    menu = Menu.objects.all()
    team = Team.objects.all()
    context = {
        'menu': menu,
        'team': team
    }
    return render(request, 'index.html', context=context)

def contact(request):
    return render(request, 'contact.html', context={})

def about(request):
    return render(request, 'about.html', context={})

def menu(request):
    return render(request, 'menu.html', context={})

def service(request):
    return render(request, 'service.html', context={})

def team(request):
    return render(request, 'team.html', context={})

def testimonial(request):
    return render(request, 'testimonial.html', context={})