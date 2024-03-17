from django.urls import path, include

from guitar_house.accounts.views import SignInUserView, sign_out, RegisterUserView, DetailProfileView, EditProfileView, \
    DeleteProfileView

urlpatterns = (
    path('sign-up/', RegisterUserView.as_view(), name='sign-up'),
    path('sign-in/', SignInUserView.as_view(), name='sign-in'),
    path('sign-out/', sign_out, name='sign-out'),
    path('profile/<int:pk>/', DetailProfileView.as_view(), name='profile'),
    path('edit-profile/<int:pk>/', EditProfileView.as_view(), name='edit-profile'),
    path('delete-profile/<int:pk>/', DeleteProfileView.as_view(), name='delete-profile'),
)