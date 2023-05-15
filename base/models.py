from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=50, unique=True)
    # client_email = models.CharField(max_length=50, unique=True)
    # password = models.CharField(max_length=50)
    # created_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50)
    project_desc = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name


# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=50)
#     user_email = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=50)
#     # project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     created_date = models.DateField(auto_now_add=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return self.user_name


# class UserProjects(models.Model):
#     user_project_id = models.AutoField(primary_key=True)
#     user_id = models.IntegerField()
#     project_id = models.IntegerField()
#     created_date = models.DateField(auto_now_add=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('user_id', 'project_id').


{
    "project_name": "Project A",
    "users": [
        {
            "id": 1,
            "name": "admin"
        }
    ]
}
