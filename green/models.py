from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

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
    email=models.EmailField(unique=True)
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




        


class UserDetails(models.Model):
    profile=models.OneToOneField('Profile',on_delete=models.CASCADE,null=True,blank=True)
    address=models.TextField(null=True, blank=True)
    gender=models.CharField(max_length=10, blank=True, null=True)
    age=models.IntegerField(blank=True, null=True,)
    aadhar_no=models.IntegerField(null=True, blank=True)
    blood_group=models.CharField(max_length=15, null=True, blank=True)
    academic_year=models.IntegerField(null=True, blank=True)
    def __str__(self):  
              return self.profile.username     

   
class coordinatorDetail(models.Model):
      profile=models.OneToOneField('Profile',on_delete=models.CASCADE)
      address=models.TextField()
      gender=models.CharField(max_length=10, blank=True, null=True)
      age=models.IntegerField(blank=True, null=True)


      def __str__(self):  
              return self.profile.username     



        




