from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from sms_app.models import CustomUser, Staffs, Courses, Students


########################### Python Module Import ######################

from datetime import datetime

###############################     END     ###########################

def adminHome(request):
    return render(request, 'hod_templates/home_content.html')


##################### Create Staff & Save ##########################
####################################################################

def addStaff(request):
    return render(request, 'hod_templates/add_staff_template.html')


def addStaffSave(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    
    else:
        # data = request.POST
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        
        ########### Add Staff Member Email, Password, username, first_name, last_name : for Login#######
        try:
            user = CustomUser.objects.create_user(
                username = username, 
                email = email, 
                password = password, 
                first_name = first_name, 
                last_name = last_name, 
                user_type = 2,
            )
            user.staffs.address = address
            # print(user)
            user.save()
            messages.success(request, "Successfully Added")
            return HttpResponseRedirect("/add_staff")
        
        except:
            messages.error(request, "Failed To Add !!")
            return HttpResponseRedirect("/add_staff")
        
        
##################### Create Course  ################################
#####################################################################

def addCourse(request):
    return render(request, "hod_templates/add_course_template.html")


def addCourseSave(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    
    else:
        course_name = request.POST.get("course_name")
        
        try:
            course = Courses(course_name = course_name)
            print(course)
            course.save()
            messages.success(request, "Successfully Added")
            return HttpResponseRedirect("/add_course")
        
        except:
            messages.error(request, "Failed !!")
            return HttpResponseRedirect("/add_course")
    

##################### Add Student & Save ##########################
#####################################################################

def addStudent(request):
    courses = Courses.objects.all()
    return render(request, "hod_templates/add_student_template.html", {"courses": courses})


def addStudentSave(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        course_id = data.get("course_name")
        sex = data.get("sex")
        email = data.get("email")
        password = data.get("password")
        address = data.get("address")
        session_start_year = data.get("session_start_year")
        session_end_year = data.get("session_end_year")
        
        ########### Add Student Email, Password, username, first_name, last_name : for Login#######
        try:
            user = CustomUser.objects.create_user(username = username, 
                                                  email = email, 
                                                  password = password, 
                                                  first_name = first_name, 
                                                  last_name = last_name, 
                                                  user_type = 3,
                                                  )
            # Getting Course Id from Course table
            user.students.course_id = Courses.objects.get(id = course_id)
            user.students.address = address
            user.students.sex = sex
            user.students.session_start_year = session_start_year
            user.students.session_end_year = session_end_year
            
            print(user)
            user.save()
            messages.success(request, "Successfully Added")
            return HttpResponseRedirect("/add_student")
        
        except Exception as e:
            print(e)
            messages.error(request, f"Failed To Add !! Because ({e})")
            return HttpResponseRedirect("/add_student")