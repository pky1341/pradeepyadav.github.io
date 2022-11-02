from django.shortcuts import render

from portfolioapp.models import (About, Contact, Etc, Image, Inf, Principle,
                                 Singing, Tutorial)


# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    im=Image.get_all_photos()  # type: ignore
    return render(request,'home.html',{'im':im})
def work(request):
    im=Image.get_all_photos()
    return render(request,"work.html",{'im':im})
def about(request):
    det=About.get_all_details()
    return render(request,"about.html",{'det':det})
def tutorial(request):
    val=Tutorial.get_all_values()
    return render(request,"tutorial.html",{'val':val})
def notes(request):
    return render(request,"notes.html")
def contact(request):
    try:
        if request.method=="POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            num=request.POST.get('num')
            sug=request.POST.get('sug')
            
            contact=Contact(name=name,email=email,phone=num,suggest=sug)
            contact.save()
    except:
        pass
    return render(request,"contact.html")
def etc(request):
    et=Etc.get_all_etc()
    return render(request,"etc.html",{'et':et})
def inf(request):
    infes=Inf.get_all_infor()
    return render(request,"inf.html",{'infes':infes})
def design(request):
    return render(request,"design.html")
def web_design(request):
    return render(request,"web_design.html")
def singing(request):
    cont=Singing.get_all_content()
    return render(request,"singing.html",{'cont':cont})
def principle(request):
    add=Principle.objects.all()
    return render(request,"principle.html",{'add':add})
def nacessary(request):
    return render(request,"nacessary.html")