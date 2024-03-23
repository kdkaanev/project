from django.urls import path

from guitar_house.guitar.views import DetailGuitarView, CreateGuitarView, ReviewGuitarsView, EditGuitarView, \
    DeleteGuitarView, add_review

urlpatterns = (
    path('details/<int:pk>/', DetailGuitarView.as_view(), name='guitar-info'),
    path('add/',  CreateGuitarView.as_view(), name='guitar-add'),
    path('reviews/<int:pk>/', ReviewGuitarsView.as_view(), name='guitar-reviews'),
    path('edit/<int:pk>/', EditGuitarView.as_view(), name='guitar-edit'),
    path('delete/<int:pk>/', DeleteGuitarView.as_view(), name='guitar-delete'),
    path('review/<int:guitar_id>/add', add_review, name='add-review'),



)