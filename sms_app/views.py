from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseRedirect
from sms_app.email_backend import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def demo(request):
    return render(request, 'demo.html')

def loginPage(request):
    return render(request, 'login_page.html')


#*********************Login & Show Details***********************
#################################################################


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Login Failed !! Method Not Allowed.</h2>")
    else:
        # Getting username and password
        username = request.POST.get("email")
        password = request.POST.get("password")
        
        user = EmailBackEnd.authenticate(request, username = username, password = password)
        
        # Creating string for email & password for debugging purpose
        # email = "Email: " + username
        # password = "Password: " + password
        
        # Checking username and password are correct then login
        if user != None:
            login(request, user)
            return HttpResponseRedirect('/admin_home')

        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")
        
        
def getUserDetails(request):
    if request.user != None: 
        return HttpResponse("User : " + request.user.email + "usertype: "+request.user.user_type)
    else : 
        return HttpResponse("Please Login First")
    
    
#**********************User Logout**************************        
############################################################

def userLogout(request):
    logout(request)
    return HttpResponseRedirect("/")
    