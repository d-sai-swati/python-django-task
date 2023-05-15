from django.core import serializers
from django.http import JsonResponse
from django.utils.functional import SimpleLazyObject
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
import datetime
from django.contrib.auth.models import User



# Create your views here.


class ClientsCRUD(APIView):
    def get(self, request, id=None):

        clients_list = list(Client.objects.values())
        return Response({"data": clients_list})

    def post(self, request, id=None):
        try:
            data = request.data
            client_name = data["client_name"]
        except Exception as e:
            return Response({"msg": "Check The Json Object Keys While Sending the Data..Error is"+str(e)})
        else:
            user = request.user.id
            if user is None:
                user = client_name = data["created_by"]
            print('user ',user)
            date = datetime.datetime.now()
            try:
                Client.objects.create(client_name=client_name, created_by=user)
                msg = "Created"
            except Exception as e:
                return Response({"msg": "Error while creating the Data..Error is"+str(e)})
            return Response({"msg": msg})


class ClientsCRUD1(APIView):
    def get(self, request, id=None):

        if id:
            clients_list = list(Client.objects.filter(
                client_id=id).values())
            my_dict = {}
            if clients_list:
                my_dict = clients_list[0]
            return Response(my_dict)
        else:
            clients_list = list(Client.objects.values())
            return Response({"data": clients_list})

    def put(self, request, id=None):
        try:
            data = request.data
            client_name = data["client_name"]
        except Exception as e:
            return Response({"msg": "Check The Json Object Keys While Sending the Data..Error is"+str(e)})
        else:
            user = request.user
            date = datetime.datetime.now()
            client = Client.objects.filter(client_id=id)
            try:
                client.update(
                    client_name=client_name,  updated_at=date, created_by=user)
                msg = "Updated"
            except Exception as e:
                return Response({"msg": "Error while creating the Data..Error is"+str(e)})
            return Response({"msg": msg})

    def delete(self, request, id=None):
        if id:
            user = request.user
            date = datetime.datetime.now()
            client = Client.objects.filter(client_id=id)
            if client:
                client.delete()
                msg = "Deleted"
            else:
                msg = "Not Deleted"
            return Response({"msg": msg}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"msg": None})


class Projects(APIView):
    def post(self, request, id=None):
        try:
            data = request.data
            project_name = data["project_name"]
            users = data["users"]
        except Exception as e:
            return Response({"msg": "Check The Json Object Keys While Sending the Data..Error is"+str(e)})
        else:
            user1 = request.user
            date = datetime.datetime.now()
            print(type(user1), "uuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
            user2 = User.objects.get(pk=request.user.pk)
            print(user2, "ooooooooooooo")
            for user in users:
                user_id = user["id"]
                user_name = user["name"]
                user2 = User.objects.get(pk=user_id)
                print(user2, user2.username, "iiiiiiiiiiiiiiiiiii")
                try:
                    # Project.objects.create(
                    #     project_name=project_name, project_desc=project_name, client_id=id, created_date=date, timestamp=date,
                    #     created_by=user2
                    # )
                    # user_json = json.dumps(user2)

                    client = Client.objects.get(client_id=id)
                    project = Project()
                    project.project_name = project_name
                    project.project_desc = project_name
                    project.client = client
                    project.created_date = date
                    project.timestamp = date
                    project.created_date = date
                    project.created_by.user = user2

                    project.save()
                    msg = "Created"
                except Exception as e:
                    return Response({"msg": "Error while creating the Data..Error is"+str(e)})
            project = Project.objects.last()
            project_id = project.project_id
            client_name = project.client.client_name
            created_by = project.created_by
            timestamp = project.timestamp
            my_dict = {}
            my_dict.update({"id": project_id, "project_name": project_name,
                           "client": client_name, "created_at": timestamp, "created_by": created_by})

            return Response(my_dict)


class ProjectsList(APIView):
    def get(self, request, id=None):
        user = request.user
        projects = list(Project.objects.filter(created_by_id=user.pk).values())
        return Response({"data": projects})
