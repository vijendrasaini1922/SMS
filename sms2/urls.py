from django.contrib import admin
from django.urls import path
from sms2 import settings
from django.conf.urls.static import static
from sms_app import views, views_hod

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginPage),
    path('do_login', views.doLogin),
    path('get_user_details', views.getUserDetails),
    path('user_logout/', views.userLogout),
    path('admin_home', views_hod.adminHome),
    path('add_staff', views_hod.addStaff),
    path('add_staff_save', views_hod.addStaffSave),
    path('add_course', views_hod.addCourse),
    path('add_course_save', views_hod.addCourseSave),
    path('add_student', views_hod.addStudent),
    path('add_student_save', views_hod.addStudentSave),
    

    # path('demo/', views.demo),   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)