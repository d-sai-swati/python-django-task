# Generated by Django 4.2.1 on 2023-05-15 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProjects',
            fields=[
                ('user_project_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('project_id', models.IntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'unique_together': {('user_id', 'project_id')},
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=50)),
                ('project_desc', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.client')),
            ],
        ),
    ]
