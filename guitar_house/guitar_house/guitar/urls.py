from django.urls import path

from guitar_house.guitar.views import DetailGuitarView

urlpatterns = (
    path('details/<int:pk>/', DetailGuitarView.as_view(), name='guitar-info'),
)