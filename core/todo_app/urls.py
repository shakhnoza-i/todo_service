from django.urls import path, include
from todo_app.views import TaskListAV, TaskDetailAV


urlpatterns = [
    path('', TaskListAV.as_view(), name='task-list'),
    path('<int:pk>/',  TaskDetailAV.as_view(), name='task-details'),
]
