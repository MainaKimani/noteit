# Generated by Django 4.1.5 on 2023-01-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]