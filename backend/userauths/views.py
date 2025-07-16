from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
import shortuuid

from userauths.models import User, Profile
from userauths.serializers import MyTokenObtainPairSerializer, RegisterSerializer, UserSerializer


# Create your views here.
#  this is for token generate view
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



########################################################
#---------------------REGISTER -------------------------#
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer



########################################################
#---------------------PASSWORD RESET -------------------------#
def generate_otp():
    uuid_key = shortuuid.uuid()  # generate string - nljsndosndono3el24l4rltlnln5l6n5kjnlrlel
    unique_key = uuid_key[:6]   # select first 6 - nljsnd
    return unique_key


# here will will retrivr api one user to change password
class PasswordResetEmailVerify(generics.RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

    # first we get user email id so we can send message
    def get_object(self):
        email = self.kwargs['email']
        user = User.objects.get(email=email)
        print("user ====", user)

        if user:
            user.otp = generate_otp()
            user.save()

            uidb64 = user.pk
            otp = user.otp

            link = f"http://localhost:5173/create-new-password?otp={otp}&uidb64={uidb64}"


            # send email
        
        return user

    
