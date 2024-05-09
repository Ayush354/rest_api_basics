from django.urls import path
from . import views

urlpatterns = [
    path('emp/', views.employeeView, name="employeeview"),
    path('student/', views.student_list, name="student_list"),
    path('student/<int:pk>', views.student_detail, name="student_detail"),
    path('passenger/', views.passenger_list, name="passenger_list"),
    path('passenger/<int:pk>', views.passenger_detail, name="passenger_detail"),

]
