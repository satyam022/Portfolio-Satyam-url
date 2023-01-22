from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.views import generic


# Create your views here.


def Index(request):
    certificate = Certificate.objects.all()
    userprofile = UserProfile.objects.filter()
    skill = Skill.objects.filter()
    portfolio = Portfolio.objects.all()
    projectwork = ProjectWork.objects.all()
    experiencework = ExperienceWork.objects.all()
    blogpage = BlogPage.objects.all()
    aboutprofile = Aboutprofile.objects.filter()
    achievement =Achievement.objects.all()

    context = {
        'skill': skill,
        'Userprofile': userprofile,
        'certificate': certificate,
        'portfolio': portfolio,
        'projectwork': projectwork,
        'experiencework': experiencework,
        'blogpage': blogpage,
        'aboutprofile': aboutprofile,
        'achievement':achievement,
    }
    return render(request, 'index.html', context)


def Base(request):
    return render(request, 'base.html')


def Port_folio(request):
    projectwork = ProjectWork.objects.all()
    context ={
        'projectwork': projectwork,
    }
    return render(request, 'portfolio.html',context)


def Blog(request):
    blogpage = BlogPage.objects.all()
    context={
        'blogpage':blogpage,
    }
    return render(request, 'blog.html',context)



def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if len(name) < 2 or len(email) < 3 or len(message) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contex = ContactProfile(name=name, email=email, message=message)
            contex.save()
            messages.success(request, "Thank you. We will be in touch soon.")
    return render(request, 'contact.html')


# Create your views here.

