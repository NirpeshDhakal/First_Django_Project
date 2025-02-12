from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Classroom, Student, StudentProfile

@login_required

def classroom_view(request):
    queryset=Classroom.objects.all()
    search=request.GET.get("search")
    if search:
        queryset=queryset.filter(name__icontains=search)
    section=request.GET.get("section")
    if section:
        queryset=queryset.filter(section=section.upper())    
    paginator=Paginator(queryset,5)

    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request, template_name="crud/classroom.html", 
                  context={"page_obj":page_obj})


def add_classroom_view(request):
    if request.method == "POST":
        print(request.POST)
        classroom_name = request.POST.get("classroom_name")
        section = request.POST.get("classroom_section")
        Classroom.objects.create(name=classroom_name, section=section)
        return redirect("crud_classroom")
    return render(request, template_name="crud/add_classroom.html")


def update_classroom_view(request,id):
    classroom = Classroom.objects.get(id=id)
    print(classroom.name)
    print(classroom.section)
    if request.method == "POST":
        classroom_name = request.POST.get("classroom_name")  # This data from HTML form
        section = request.POST.get("classroom_section")  # This data from HTML form
        classroom.name = classroom_name  # set data to classroom object
        classroom.section = section  # set data to classroom object
        classroom.save()  # This actually commit / store data to the table
        return redirect("crud_classroom")
    return render(request, template_name="crud/update_classroom.html", context={"classroom": classroom})

def delete_classroom_view(request,id):
    classroom=Classroom.objects.get(id=id)
    if request.method == "POST":
        classroom.delete()
        return redirect("crud_classroom")
    return render(request,template_name="crud/delete_confirmation.html",context={"classroom":classroom})

def student_view(request):
    return render(request, template_name="crud/student.html", 
                  context={"students": Student.objects.all()})

def add_student_view(request):
    if request.method =="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        email=request.POST.get("email")
        address=request.POST.get("address")
        classroom_id=request.POST.get("classroom")
        Student.objects.create(name=name,age=age,email=email,address=address,classroom_id=classroom_id)
        return redirect("crud_student")
    return render(request, template_name="crud/add_student.html",context={"students":Student.objects.all(), 
                                                                          "classrooms":Classroom.objects.all()})

def update_student_view(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        address = request.POST.get("address")
        student_id = request.POST.get("student")
        Student.objects.filter(id=id).update(name=name, age=age, email=email, address=address, student_id=student_id)
        return redirect("crud_student")
    return render(request, template_name="crud/update_student.html", 
                  context={"classrooms": Classroom.objects.all(), "student": student})

def delete_student_view(request,id):
    student=Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect("crud_student")
    return render(request,template_name="crud/delete_confirmation.html",context={"student":student})

def student_profile_view(request):
    return render(request,template_name="crud/student_profile.html",context={"profiles":StudentProfile.objects.all()})


def add_student_profile_view(request):
    if request.method == "POST":
        student_id=request.POST.get("student_id")
        phone=request.POST.get("phone")
        roll=request.POST.get("roll")
        bio=request.POST.get("bio")
        pp=request.FILES.get("pp")
        sp=StudentProfile.objects.create(student_id=student_id,phone=phone,roll=roll,bio=bio)
        if pp:
            sp.profile_picture=pp 
            sp.save()
        return redirect("student_profile")
    



    return render(request,template_name="crud/add_student_profile.html",context={"students":Student.objects.all()})

def student_profile_detail_view(request):
    profile=StudentProfile.objects.get(id=id)
    return render(request,template_name="crud/student_profile_detail.html",context={"profile":profile})



class UserloginView(View):
    def get(self,*args,**kwargs):
        return render(self.request,template_name="crud/user_login.html")
    

    def post(self,*args,**kwargs):
        un=self.request.POST["username"]
        pw=self.request.POST["password"]
        user=authenticate(username=un,password=pw)
        if user:
            login(self.request,user)
            messages.success(self.request,"user logged in!")
            next_url=self.request.GET.get("next")
            if next_url:
                  return redirect(next_url)
            else:
                return redirect("crud_classroom")
        else:
            messages.error(self.request,"could not login.Invalid credential!")
            return redirect("user_login")
   
def user_logout_view(request):
    logout(request)
    return redirect("user_login")


