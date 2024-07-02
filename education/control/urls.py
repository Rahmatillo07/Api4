from django.urls import path, include

from .views import (CourseViewCreate, CourseDetailUpdateView, CourseDetailDeleteView, TeacherViewCreate,
                    TeacherDetailUpdateView,
                    TeacherDetailDeleteView, StudentViewCreate, StudentDetailUpdateView, StudentDetailDeleteView)

urlpatterns = [
    path('api/v1/courses/', CourseViewCreate.as_view()),
    path('api/v1/course/<int:pk>/', CourseDetailUpdateView.as_view()),
    path('api/v1/course/<int:pk>/', CourseDetailDeleteView.as_view()),
    path('api/v1/teachers/', TeacherViewCreate.as_view()),
    path('api/v1/teacher/<int:pk>/', TeacherDetailUpdateView.as_view()),
    path('api/v1/teacher/<int:pk>/', TeacherDetailDeleteView.as_view()),
    path('api/v1/students/', StudentViewCreate.as_view()),
    path('api/v1/students/<int:pk>/', StudentDetailUpdateView.as_view()),
    path('api/v1/students/<int:pk>/', StudentDetailDeleteView.as_view()),

    path('api-auth/', include('rest_framework.urls'))
]
