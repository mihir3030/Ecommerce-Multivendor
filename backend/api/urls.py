from django.urls import path
from userauths import views as userauths_views
from store import views as store_views

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('user/token/', userauths_views.MyTokenObtainPairView.as_view()),
    path('user/token/refresh', TokenRefreshView.as_view()),  # when hit this it will give us new refresh token
    path("user/register/", userauths_views.RegisterView.as_view()),
    path("user/password-reset/<str:email>/", userauths_views.PasswordResetEmailVerify.as_view()),
    path("user/password-change/", userauths_views.PasswordChangeView.as_view(), name="password-change"),


    # STORE endpoints
    path("category/", store_views.CategoryListView.as_view()),
    path("products/", store_views.ProductListView.as_view()),
    path("products/<slug>/", store_views.ProductDetailAPIView.as_view()),
]