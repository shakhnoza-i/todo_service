from todo_app.models import Task
from todo_app.serializers import (TaskSerializer, TaskSerializerAll,
                                  TaskSerializerComplete)
from todo_app.tasks import send_mail_func
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TaskListAV(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializerAll(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class TaskDetailAV(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'ERROR':"Task not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializerAll(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = Task.objects.get(pk=pk) 
        status1 = task.completed
        serializer = TaskSerializerAll(task, data=request.data)
        current_email = request.user.email
        print(f"current_email: {current_email}")
        if serializer.is_valid():
            serializer.save()
            status2 = task.completed
            if status1 != status2:
                send_mail_func.delay(current_email)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):     
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
