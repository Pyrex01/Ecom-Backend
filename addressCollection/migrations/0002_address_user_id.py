# Generated by Django 3.2.9 on 2021-12-21 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addressCollection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
