# Generated by Django 3.2.5 on 2022-05-05 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220505_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='recept_id',
        ),
        migrations.AddField(
            model_name='user',
            name='recept_id',
            field=models.ManyToManyField(blank=True, to='main.Recepts'),
        ),
    ]
