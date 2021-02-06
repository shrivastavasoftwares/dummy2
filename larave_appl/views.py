from django.shortcuts import render
from rest_framework import viewsets
from larave_appl.models import Employee_info,State
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from larave_appl.serializers import State_serializer,EmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
# Create your views here.
class Stat_views(viewsets.ViewSet):
    http_method_names = ['post','get']

    def create(self,request):

        serializers=State_serializer(data=request.data)
        if serializers.is_valid():

            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
    def list(self,request):
        queryset=State.objects.all()
        serializer=State_serializer(queryset,many=True)
        print(serializer.data,']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        return Response(serializer.data)







class Employee_view(viewsets.ViewSet):

    def create(self,request):



        serializers=EmployeeSerializer(data=request.data)
        if serializers.is_valid():

            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)




class search_emp(viewsets.ModelViewSet):

    queryset = Employee_info.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields =('Team_leader','Bank','Branch_name','Branch_code','Emp_name','Phone_no','email','designation','CTC','State','District','Location','Alternative_Phone_no','Cluster_head','grade')





