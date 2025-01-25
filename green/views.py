from django.shortcuts import render
from .models import Profile,StudentDetails,RoleChoices,coordinatorDetail
from .forms import StudentDetailsForm
from django.shortcuts import render,redirect
 

# Create your views here.


def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def userregistration(request):
    return render(request,"userregistration.html")


def edit_teacherform(request):
    return render(request,"edit_teacherform")


# def coordinator_registration(request):
    # return render(request,"coordinator_reg.html")


def user_registration(request):
    name=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")
    firstname=request.POST.get("firstname")
    lastname=request.POST.get("lastname")

    student_form=StudentDetailsForm(request.POST)
    try:
        user=Profile.objects.create_user(username=name,role=RoleChoices.user,email=email,password=password,first_name=firstname,last_name=lastname)
    except Exception as e:
        print(e)
        return redirect('user_registration')
    
    if student_form.is_valid():
        user_details = student_form.save(commit=False)
        user_details.profile = user
        user_details.save()
    return render(request,'userregistration')


def admin_dashboard(request):
    return render(request,"admin_dashboard.html")


def user_dashboard(request):
    return render(request,"user_dashboard.html")

 
def coordinator_dashboard(request):
    return render(request,"coordinator_dashboard.html")


def manage_appoinment(request):
    return render(request,"manage_appoinment.html")

  



def admin_appoinment(request):
    return render(request,"admin_appoinment.html")


def edit_teacherform(request):
    return render(request,"edit_teacherform.html")


# Create the view function
def teacher_registration(request):
    if request.method == 'POST':
        # Retrieve the form data
        name = request.POST.get('name')
        user_id = request.POST.get('userId')
        college = request.POST.get('college')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        coordinatorDetail.objects.create(name=name, user_id=user_id, college=college, phone=phone, email=email)
    return render(request, 'teacher_registration.html')


def studentdetails_table(request):
    return render(request,"studentdetails_table.html")
  


def studentdetailsadd_table(request):
    return render(request,"studentdetailsadd_table.html")


    
def studentdetailsadd_table(request):
    if request.method == 'POST':
        # Retrieve the form data
        enrollment_no = request.POST.get('enrollment-no')
        year = request.POST.get('year')
        name = request.POST.get('name')
        guardian = request.POST.get('guardian')
        aadhaar = request.POST.get('aadhaar')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        gender = request.POST.get('gender')
        course = request.POST.get('course')
        blood_group = request.POST.get('blood-group')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        remarks = request.POST.get('remarks')
        StudentDetails.objects.create(enrollment_no=enrollment_no ,name=name, guardian=guardian, aadhaar=aadhaar, dob=dob, category=category, gender=gender, course=course, blood_group=blood_group, address=address, remarks=remarks)
    return render(request, "studentdetailsadd_table.html")


def manageactivity_table(request):
    return render(request,"manageactivity_table.html")

def manageactivityadd(request):
    return render(request,"manageactivityadd.html")
 
def feedbacktable(request):
    return render(request,"feedbacktable.html")

def feedbacktableadd(request):
    return render(request,"feedbacktableadd.html")

def attendance(request):
    return render(request,"attendance.html")

def attendanceadd(request):
    return render(request,"attendanceadd.html")

def certificate(request):
    return render(request,"certificate.html")