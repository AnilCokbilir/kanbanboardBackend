from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from task.views import TasksViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    
]
