import profile

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from guitar_house import settings
from guitar_house.accounts.models import Profile
from django.core.mail import send_mail

UserModel = get_user_model()



def send_welcome_email(user):
    html_message = render_to_string(
        'email/email-greeting.html',
        {
            'profile': user
        }


    )
    plain_message = strip_tags(html_message)
    send_mail(
        subject='Registration greatings',
        message=plain_message,
        html_message=html_message,
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=(user.email,),
    )

@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):

    if not created:
        return

    Profile.objects.create(user=instance)
    send_welcome_email(user=instance)

