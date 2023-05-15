# Generated by Django 4.2.1 on 2023-05-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_by',
            field=models.CharField(default='--', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]