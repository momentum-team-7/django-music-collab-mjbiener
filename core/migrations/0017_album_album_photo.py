# Generated by Django 3.1.7 on 2021-03-02 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20210302_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_photo',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]