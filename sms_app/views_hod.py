from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from sms_app.models import CustomUser, Staffs, Courses, Students, Subjects


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
        
        
def manageStaff(request):
    staffs = Staffs.objects.all()
    return render(request, "hod_templates/manage_staff_template.html", {"staffs" : staffs})
        

##################### Add Student & Save ##########################
#####################################################################

def addStudent(request):
    courses = Courses.objects.all()
    # for i in courses:
        # print(i)
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
        gender = data.get("gender")
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
            # print(Courses.objects.get(id = course_id))
            user.students.course_id = Courses.objects.get(id = course_id)
            user.students.address = address
            user.students.gender = gender
            # print(sex)
            user.students.session_start_year = session_start_year
            # print(session_start_year)
            # print(user.students.session_start_year)
            user.students.session_end_year = session_end_year
            
            # print(user)
            user.save()
            messages.success(request, "Successfully Added")
            return HttpResponseRedirect("/add_student")
        
        except Exception as e:
            # print(e)
            messages.error(request, f"Failed To Add !! Because ({e})")
            return HttpResponseRedirect("/add_student")
        

def manageStudent(request):
    students = Students.objects.all()
    return render(request, "hod_templates/manage_student_template.html", {"students" : students})


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
    

def manageCourse(request):
    courses = Courses.objects.all()
    return render(request, "hod_templates/manage_course_template.html", {"courses" : courses})


##################### Create Subject  ################################
#####################################################################

def addSubject(request):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    for i in staffs:
        print(i.first_name, i.last_name, i.id)
    return render(request, "hod_templates/add_subject_template.html",
                  {"courses" : courses, "staffs": staffs})


def addSubjectSave(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    
    else:
        data = request.POST
        subject_name = data.get("subject_name")
        # print(subject_name)
        ## Here we get id when we fetch
        course_id = data.get("course_id")
        staff_id = data.get("staff_id")
        print(course_id)
        print(staff_id)
        
        try:
            ## Course id, staff id instance creating from Courses, Staffs class
            course_instance = Courses.objects.get(id=course_id)
            staff_instance = CustomUser.objects.get(id=staff_id)
            print(course_instance)
            print(staff_instance)
                
        except (Courses.DoesNotExist, Staffs.DoesNotExist):
            messages.error(request, "Course or Staff Doesn't Exist")
            return HttpResponseRedirect("/add_subject")
            
        try:
            subject = Subjects(subject_name=subject_name,
                               course_id=course_instance,
                               staff_id=staff_instance)
            
            subject.save()
            messages.success(request, "Successfully Added")
            return HttpResponseRedirect("/add_subject")
            
        except Exception as e:
            messages.error(request, f"Failed due to error : ({e})")
            return HttpResponseRedirect("/add_subject")
              

def manageSubject(request):
    subjects = Subjects.objects.all()
    return render(request, "hod_templates/manage_subject_template.html", {"subjects": subjects})


##################### View Attendance ################################
######################################################################

def viewAttendance(request):
    #TODO
    return render(request, "hod_templates/view_attendance_template.html")


##################### Feedback ######################################
#####################################################################

def feedbackStudent(request):
    #TODO
    return render(request, "hod_templates/feedback_student_template.html")

def feedbackStaff(request):
    #TODO
    return render(request, "hod_templates/feedback_staff_template.html")


##################### Leave #########################################
#####################################################################

def leaveStudent(request):
    #TODO
    return render(request, "hod_templates/leave_student_template.html")

def leaveStaff(request):
    #TODO
    return render(request, "hod_templates/leave_staff_template.html")