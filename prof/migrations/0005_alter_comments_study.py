# Generated by Django 4.1.5 on 2023-01-10 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0004_alter_comments_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='study',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='prof.study'),
        ),
    ]