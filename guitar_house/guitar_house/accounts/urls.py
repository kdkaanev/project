from django.urls import path

from guitar_house.accounts.views import SignUpUserView, SignInUserView, sign_out

urlpatterns = (
    path('sign-up/', SignUpUserView.as_view(), name='sign-up'),
    path('sign-in/', SignInUserView.as_view(), name='sign-in'),
    path('sign-out/', sign_out, name='sign-out'),
)