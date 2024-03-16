from django.urls import path, include

from guitar_house.accounts.views import SignInUserView, sign_out, RegisterUserView, DetailProfileView

urlpatterns = (
    path('sign-up/', RegisterUserView.as_view(), name='sign-up'),
    path('sign-in/', SignInUserView.as_view(), name='sign-in'),
    path('sign-out/', sign_out, name='sign-out'),
    path('profile/<int:pk>/', DetailProfileView.as_view(), name='profile'),
)