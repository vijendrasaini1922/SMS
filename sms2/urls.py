from django.contrib import admin
from django.urls import path
from sms2 import settings
from django.conf.urls.static import static
from sms_app import views, views_hod

urlpatterns = [
    ############# Admin Login / Logout ###########
    path('admin/', admin.site.urls),
    path('', views.loginPage),
    path('do_login', views.doLogin),
    path('get_user_details', views.getUserDetails),
    path('user_logout/', views.userLogout),
    
    
    ############### Admin HOME ##################
    path('admin_home', views_hod.adminHome),
    
    
    ################# Staff ######################
    path('add_staff', views_hod.addStaff),
    path('add_staff_save', views_hod.addStaffSave),
    path('manage_staff/', views_hod.manageStaff),
    
    
    ################# Student ####################
    path('add_student', views_hod.addStudent),
    path('add_student_save', views_hod.addStudentSave),
    path('manage_student', views_hod.manageStudent),
    
    
    ################# Course #####################
    path('add_course', views_hod.addCourse),
    path('add_course_save', views_hod.addCourseSave),
    path('manage_course', views_hod.manageCourse),
    
    
    ################# Subject ####################
    path('add_subject', views_hod.addSubject),
    path('add_subject_save', views_hod.addSubjectSave),
    path('manage_subject', views_hod.manageSubject),
    
    
    ############### View Attendance ###############
    path('view_attendance', views_hod.viewAttendance),

    
    ################# Feedback ####################
    path('feedback_student', views_hod.feedbackStudent),
    path('feedback_staff', views_hod.feedbackStaff),
    
    
    ################### Leave ######################
    path('leave_student', views_hod.leaveStudent),
    path('leave_staff', views_hod.leaveStaff),
    


    ################ Test Cases ####################
    # path('demo/', views.demo),   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)