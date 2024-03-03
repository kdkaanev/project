from django.urls import path

from guitar_house.guitar.views import DetailGuitarView, CreateGuitarView

urlpatterns = (
    path('details/<int:pk>/', DetailGuitarView.as_view(), name='guitar-info'),
    path('add/',  CreateGuitarView.as_view(), name='guitar-add'),
)