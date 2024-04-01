from django.urls import path

from guitar_house.common import views

urlpatterns = (
    path('', views.index, name='index'),
    path('guitars/', views.show_guitars, name='guitars'),
    path('user-guitars/', views.user_guitars, name='user-guitars'),
    path('<int:guitar_id>/contact/', views.contact_seller, name='messages'),
    path('messages/', views.sent_messages, name='show-messages'),
    path('reply/<int:message_id>/', views.reply_message, name='reply-message'),
    path('delete-message/<int:message_id>/', views.delete_message, name='delete-message'),
)
