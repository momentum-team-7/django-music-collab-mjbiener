# Generated by Django 3.1.7 on 2021-03-01 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_album_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL),
        ),
    ]
