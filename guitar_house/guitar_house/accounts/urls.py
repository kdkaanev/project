from django.urls import path

from guitar_house.accounts.views import SignInUserView, sign_out, RegisterUserView

urlpatterns = (
    path('sign-up/', RegisterUserView.as_view(), name='sign-up'),
    path('sign-in/', SignInUserView.as_view(), name='sign-in'),
    path('sign-out/', sign_out, name='sign-out'),
)