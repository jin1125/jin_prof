# Generated by Django 4.1.5 on 2023-01-09 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careerslist',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='careers_list', to='prof.profile'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='prof.profile'),
        ),
    ]
