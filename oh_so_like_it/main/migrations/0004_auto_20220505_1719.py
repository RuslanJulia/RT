# Generated by Django 3.2.5 on 2022-05-05 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220504_1000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sub_category',
            options={'verbose_name_plural': 'Подкатегории'},
        ),
        migrations.AddField(
            model_name='user',
            name='recept_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.recepts'),
        ),
    ]
