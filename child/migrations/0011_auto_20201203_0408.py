# Generated by Django 2.2.6 on 2020-12-02 22:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('child', '0010_esehi_uperms'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='esehi',
            new_name='Member',
        ),
    ]
