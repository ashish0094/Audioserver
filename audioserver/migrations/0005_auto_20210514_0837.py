# Generated by Django 3.2.2 on 2021-05-14 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioserver', '0004_delete_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='AudioID',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='PodID',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='SongID',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
    ]
