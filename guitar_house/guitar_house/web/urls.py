from django.urls import path

from guitar_house.web import views

urlpatterns = (
    path('', views.index, name='index'),
    path('guitars/', views.show_guitars, name='guitars'),
    path('user-guitars/', views.user_guitars, name='user-guitars'),
)
