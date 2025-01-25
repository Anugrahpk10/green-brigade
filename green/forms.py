
from django import forms
<<<<<<< HEAD
from .models import StudentDetails

# from .models import CoordinatorDetails

class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
=======
from .models import UserDetails
# from .models import CoordinatorDetails

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetails
>>>>>>> 06145b4548d87266d39c21653876bcdb20789920
        fields = ['profile','address', 'gender','age','aadhar_no','blood_group','academic_year']

# class CoordinatorDetailsForm(forms.ModelsForm):
#     class Meta:
#         model =CoordinatorDetails
#         fields =['profile','address','gender','age']



