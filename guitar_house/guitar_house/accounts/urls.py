from django.urls import path

from guitar_house.accounts.views import Signupuserview, SignInUserView, sign_out

urlpatterns = (
    path('sign-up/', Signupuserview.as_view(), name='sign-up'),
    path('sign-in/', SignInUserView.as_view(), name='sign-in'),
    path('sign-out/', sign_out, name='sign-out'),
)