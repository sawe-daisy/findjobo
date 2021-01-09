from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
import json
from .permissions import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(APIView):
    def get(self, request, format=None): 
        serializer = UserSerializer     
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeViewSet(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format = None):
        employee = User.objects.filter(role='employee')
        serializer = UserSerializer(employee, many=True)
        return Response(serializer.data)


class EmployerViewSet(APIView):
    def get(self,request,format = None):
        employer = User.objects.filter(role='employer')
        serializer = UserSerializer(employer, many=True)
        return Response(serializer.data)
  
class JobViewSet(APIView):
    def get(self, request,format=None):      
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

class JobPostViewSet(APIView):

    # def post(self, request,format=None):
    #     permission_classes=[IsAdmin]
    #     serializer = JobSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # return Response(status=status.HTTP_400_BAD_REQUEST)

    # permission_classes= [isEmployer]
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404
    def post(self, request, id, format=None):
        user=self.get_object(id)
        if user.role=='employer':
            user=user.id
            print(user)
            serializer = JobSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

class JobDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        permission_classes = [IsAuthenticated]
        job = self.get_object(pk)
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        permission_classes = [IsAuthenticated]
        job = self.get_object(pk)
        JobSerializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ApplicationViewSet(APIView):
    def get(self,request,format = None):
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        permission_classes = [IsAuthenticated]
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  