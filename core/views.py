from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import App, Task
from .serializers import AppSerializer, TaskSerializer, UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(UserTask, id=task_id, user=request.user)
    if request.method == 'POST':
        screenshot = request.FILES.get('screenshot')
        if screenshot:
            task.screenshot = screenshot
            task.completed = True
            task.save()
            task.user.points += task.app.points
            task.user.save()
    return render(request, 'task_detail.html', {'task': task})
