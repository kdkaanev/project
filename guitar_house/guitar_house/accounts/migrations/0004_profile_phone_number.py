# Generated by Django 5.0.2 on 2024-03-16 15:57

import guitar_house.accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default=1, max_length=20, validators=[guitar_house.accounts.validators.validate_phone_number]),
            preserve_default=False,
        ),
    ]
