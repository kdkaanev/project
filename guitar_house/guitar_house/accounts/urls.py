from django.urls import path

from guitar_house.accounts.views import SignUpUserView

urlpatterns = (
    path('sign-up/', SignUpUserView.as_view(), name='sign-up'),
)