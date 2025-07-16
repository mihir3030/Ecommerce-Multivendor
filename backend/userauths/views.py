from rest_framework.response import Response
from rest_framework import status
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
            print(link)


            # send email
        
        return user

    

class PasswordChangeView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        payload = request.data

        otp = payload['otp']
        uidb64 = payload['uidb64']
        # reset_token = payload['reset_token']
        password = payload['password']

        user = User.objects.get(id=uidb64, otp=otp)
        if user:
            user.set_password(password)
            user.otp = ""
            # user.reset_token = reset_token
            user.save()

            return Response({"message": "password change succesfully"}, status=status.HTTP_201_CREATED)
        
        else:
            return Response({"message": "An error occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)