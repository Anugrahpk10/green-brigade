from django.shortcuts import render,redirect
from .models import *
from .forms import UserDetailForm
from .models import Profile

# Create your views here.


def home(request):
    return render(request,"home.html")


def login(request):
    return render(request,"login.html")



def user_registration(request):
    if request.method == "POST":
        # Fetch user details from the request
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")

        try:
            # Create the user profile
            profile = Profile.objects.create_user(
                username=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,
                role=RoleChoices.USER
            )

            # Auto-login the user after successful creation

        except Exception as e:
            # Handle error and show a message to the user
            return render(request, 'userregistration.html', {
                'error': f"Error creating user: {str(e)}",
            })

        # Create the UserDetails instance for additional information
        reg_form = UserDetailForm(request.POST)
        if reg_form.is_valid():
            user_details = reg_form.save(commit=False)
            user_details.profile = profile
            user_details.save()
            return redirect('login')  # Redirect to a success page
        else:
            print(reg_form.errors)
            return render(request, 'userregistration.html', {
                'form': reg_form,
                'error': "Please fix the errors in the form.",
            })

    # Render the registration form on a GET request
    return render(request, "userregistration.html", {
        'form': UserDetailForm()
    })

# def coordinator_registration(request):
    # return render(request,"coordinator_reg.html")




