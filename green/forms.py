
from django import forms
from .models import UserDetails
# from .models import CoordinatorDetails

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['profile','address', 'gender','age','aadhar_no','blood_group','academic_year']

# class CoordinatorDetailsForm(forms.ModelsForm):
#     class Meta:
#         model =CoordinatorDetails
#         fields =['profile','address','gender','age']



