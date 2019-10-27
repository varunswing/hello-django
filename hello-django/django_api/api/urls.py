from django.urls import path

from .college import controller as college_controller

urlpatterns = [
    path('college/get_students', college_controller.get_students)
]
