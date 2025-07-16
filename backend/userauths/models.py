from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField
from django.db.models.signals import post_save


## modified Default django user model
class User(AbstractUser):
    username = models.CharField(unique=True, max_length=20)  # username required and uniques true
    email = models.EmailField(unique=True)  # email is required and Unique
    full_name = models.CharField(max_length=100, null=True, blank=True)  # from frontend it will be required
    phone = models.CharField(max_length=20, null=True, blank=True)
    otp = models.CharField(max_length=10, null=True, blank=True)

    # username field will replace with email => email and password
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    

    # we want to save default username if none
    def save(self, *args, **kwargs):
        email_username, email_domain = self.email.split("@")
        
        if self.full_name == "" or self.full_name == None:
            self.full_name = email_username
        
        # if username is empty
        if self.username == "" or self.username == None:
            self.username = email_username

        super(User, self).save( *args, **kwargs)



# User Profile for storing information and display Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="image", default="default/default-user.png", null=True, blank=True)   # FielField => accepts all image files
    full_name = models.CharField(max_length=100, null=True, blank=True)  # from frontend it will be required
    about = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=20,null=True, blank=True)

    country = models.CharField(max_length=20,null=True, blank=True)
    state = models.CharField(max_length=20,null=True, blank=True)
    city = models.CharField(max_length=20,null=True, blank=True)
    address = models.CharField(max_length=100,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    # use pid for not exposing our Default ID to world
    # abc.com/profile/1 => abc.com/profile/adxcvg --- we use pid for security
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefghijklm")

    def __str__(self):
        if self.full_name:
            return str(self.full_name)
        else:
            return str(self.user.full_name)
        
    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name == None:
            self.full_name = self.user.full_name
        
        super(Profile, self).save(*args, **kwargs)



# When New USer Created so profile will automatic created . yah with some fields
def create_user_profile(sender, instance, created,  **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)