from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models

# Create your models here.

class RoleChoices(models.TextChoices):
    ADMIN="admin","admin"
    USER="user","user"
    COORDINATOR="coordinator","coordinator"



class gender(models.TextChoices):
    MALE="Male","Male"
    FEMALE="Female","Female"
    

class User_reg(models.Model):
    phone=models.CharField(max_length=10, null=True)
    address=models.TextField()
    gender=models.CharField(max_length=10,choices=gender.choices)

    
    def __str__(self):
        return self.phone
    


class Profile(AbstractUser):
    USERNAME_FIELD='email'
    REQUIRED_FIELD=[]

    username = models.CharField(max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    role=models.CharField(max_length=15,choices=RoleChoices.choices)
    emial=models.EmailField(unique=True)
    phone=models.CharField(max_length=15,null=True,blank=True)
    



    groups=models.ManyToManyField(
        Group,
            related_name="profile_groups",blank=True)

    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='profile_permissions',  # Change this to a unique name
        blank=True
        )

    
    def __str__(self):  
            return self.username    
    


class StudentDetails(models.Model):
    profile = models.OneToOneField('Profile', on_delete=models.CASCADE) 
    enrollment_no = models.CharField(max_length=20,null=True,blank=True)  
    year = models.PositiveIntegerField(default=2024)  
    name = models.CharField(max_length=100,null=True,blank=True)
    guardian = models.CharField(max_length=100) 
    address = models.TextField(null=True,blank=True) 
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    aadhar_no = models.BigIntegerField(null=True) 
    blood_group = models.CharField(max_length=15)  
    academic_year = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)  
    phone = models.CharField(max_length=15, blank=True)  
    email = models.EmailField(blank=True)  
    remarks = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.profile.username

   
class coordinatorDetail(models.Model):
      profile=models.OneToOneField('Profile',on_delete=models.CASCADE)
      address=models.TextField()
      gender=models.CharField(max_length=10, blank=True, null=True)
      age=models.IntegerField(blank=True, null=True)

      def __str__(self):  
              return self.profile.username     


class Certificate(models.Model):
      student=models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
      name=models.CharField(max_length=250,null=True,blank=True)
      student_class=models.CharField(max_length=250,null=True,blank=True)
      certificate=models.ImageField()

      def __str__(self):  
              return self.student.username     



class Activity(models.Model):
      name=models.CharField(max_length=250)
      category=models.CharField(max_length=250,null=True,blank=True)
      year=models.PositiveIntegerField(null=True,blank=True)
      action_plan=models.FileField(null=True,blank=True)
      action_plan_status=models.CharField(max_length=100,null=True,blank=True)


      def __str__(self):  
              return self.name    


class Feedback(models.Model):
      student=models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
      created_at=models.DateTimeField(auto_now_add=True)
      feedback=models.PositiveIntegerField(null=True,blank=True)
      activity=models.ForeignKey('activity',on_delete=models.CASCADE,null=True,blank=True)

      def __str__(self):  
              return self.name    


class Attendence(models.Model):
      student=models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
      date=models.DateField()
      status=models.CharField(max_length=100,null=True,blank=True)
      activity=models.ForeignKey('activity',on_delete=models.CASCADE,null=True,blank=True)

      def __str__(self):  
              return self.student.profile.username    


