from django.urls import path, include
from rest_framework.routers import DefaultRouter, Response
from .views import StudentViewSet
from .views import home

router = DefaultRouter()
router.register('students', StudentViewSet)

def home(request):
    return Response({"message": "Welcome to the Student API!"})

urlpatterns = [
    path('', include(router.urls)),
    path('',home, name='home'),
]