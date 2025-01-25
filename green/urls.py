from django.urls import path
from. import views





urlpatterns = [

    path("",views.home,name="home"),
    path("login/",views.login,name='login'),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("user_dashboard/",views.user_dashboard, name="user_dashboard"),
    path("coordinator_dashboard/",views.coordinator_dashboard, name="coordinator_dashboard"),
    path("userregistration/",views.userregistration, name="userregistration"),
    path("admin_appoinment/",views.admin_appoinment, name="admin_appoinment"),
    path("manage_appoinment/",views.manage_appoinment, name="manage_appoinment"),
    path("edit_teacherform/",views.edit_teacherform, name="edit_teacherform"),
    path("studentdetails_table/",views.studentdetails_table, name="studentdetails_table"),
    path("studentdetailsadd_table/",views.studentdetailsadd_table, name="studentdetailsadd_table"),
    path("manageactivity_table/",views.manageactivity_table, name="manageactivity_table"),
    path("manageactivityadd/",views.manageactivityadd, name="manageactivityadd"),
    path("feedbacktable/",views.feedbacktable, name="feedbacktable"),
    path("feedbacktableadd/",views.feedbacktableadd, name="feedbacktableadd"),
    path("attendance/",views.attendance, name="attendance"),
    path("attendanceadd/",views.attendanceadd, name="attendanceadd"),
    path("certificate/",views.certificate, name="certificate"),
    
    
    
    


    





]
