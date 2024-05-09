from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from mainapp.models import Employee, Student, Passenger
from mainapp.serializers import StudentSerializer, PassengerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def employeeView(request):
    emp={
        'id':323,
        'name':'ayush',
        'sal': 10000
    }
    data = Employee.objects.all() #its quryset and queryset cant be send diretly to jsonresponnse as it is not python object
    response ={'employee':list(data.values('name','sal'))}

    return JsonResponse(response)

@api_view(['GET','POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
        
@api_view(['GET','PUT','DELETE'])
def student_detail(request, pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer= StudentSerializer(student)
        return Response(serializer.data)    
    
    elif request.method == 'PUT':
        serializer= StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method =='DELETE':
        student.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST'])
def passenger_list(request):
    if request.method == 'GET':
        passenger = Passenger.objects.all()
        serializer = PassengerSerializer(passenger,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer=PassengerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
def passenger_detail(request,pk):
    try:
        passenger=Passenger.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer= PassengerSerializer(passenger)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer= PassengerSerializer(passenger, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
        
    elif request.method == 'DELETE':
        passenger.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

        
    