__author__ = 'PRIYANSH KHANDELWAL'
from rest_framework import serializers
from django.contrib.auth.models import User
from larave_appl.models import State,Employee_info


class State_serializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields='__all__'
        #fields=('S')



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee_info
        fields='__all__'
