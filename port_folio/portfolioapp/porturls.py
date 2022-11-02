from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),  
    path('work/',views.work,name='work'),  
    path('about/',views.about,name="about"),
    path("tutorial/",views.tutorial,name="tutorial"),
    path("notes/",views.notes,name="notes"),
    path("contact/",views.contact,name="contact"),
    path("etc/",views.etc,name="etc"), 
    path("inf/",views.inf,name="inf"),
    path("design/",views.design,name="design"),
    path("web_design/",views.web_design,name="web_design"),
    path("singing/",views.singing,name="singing") ,
    path('principle/',views.principle,name="principle"),
    path("nacessary/",views.nacessary,name="nacessary")  # type: ignore
]