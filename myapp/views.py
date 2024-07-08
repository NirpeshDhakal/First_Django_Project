from django.shortcuts import render
from django.http import HttpResponse
from crud.models import Classroom
# Create your views here.

def home_view(request):
    return HttpResponse("<h1>this is from home page</h1>")

def root_page_view(request):
    return render(request,template_name="myapp/root_page.html")
def portfolio_view(request):
    return render(request,template_name="portfolio/index.html")
def home_new_view(request):
    return render(request,template_name="myapp/root_page.html")
def learning_dtl_view(request):
    c={"name":"prixa academy" , "student":"jane"}
    return render(request,template_name="myapp/dlt.html",context=c)

  #context should always be dictionary

def using_bootstrap_view(request):
    student=[
        {"name":"jon","age":30,"email":"jon11@gmail.com","address":"ktm","display":True},
        {"name":"nirpesh","age":20,"email":"nirpesh.dhakal16@gmail.com","address":"btl","display":True},
        {"name":"rohit","age":30,"email":"rohit5@gmail.com","address":"bhw","display":False},
        {"name":"ram","age":12,"email":"ram@gmail.com","address":"ptn","display":True}

    ]



    return render(request,template_name="myapp/using_bootstrap.html",context={"student":student})
    
def temp_inherit_view(request):
    classrooms=Classroom.objects.all()
    return render(request, template_name="myapp/home.html", context={"classrooms":classrooms})

def about_us_view(request):
    return render(request,template_name="myapp/about_us.html")
def contact_us_view(request):
    return render(request,template_name="myapp/contact_us.html")


                  








    