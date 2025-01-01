from django.urls import path
from. import views





urlpatterns = [

    path("home/",views.home,name='home'),
    path("login/",views.login,name='login'),
    path("userregistration/",views.user_registration,name='userregistration'),
    # path("coordinator_registration/",views.coordinator_registration),
    


]
