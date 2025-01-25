
from django import forms
from .models import StudentDetails

# from .models import CoordinatorDetails

class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['profile','address', 'gender','age','aadhar_no','blood_group','academic_year']

# class CoordinatorDetailsForm(forms.ModelsForm):
#     class Meta:
#         model =CoordinatorDetails
#         fields =['profile','address','gender','age']



