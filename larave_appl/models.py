from django.db import models

# Create your models here.
class State(models.Model):
    State_id=models.CharField(max_length=10,unique=True,null=True,blank=True)
    State_name=models.CharField(max_length=10,null=True,blank=True,unique=True)
    def __str__(self):
        return self.State_name




class Bank(models.Model):
    Bank_id=models.CharField(max_length=10,unique=True,null=True,blank=True)
    Bank_name=models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return self.Bank_name



grade = (
    ("BM", "BM"),
    ("ABM", "ABM"),
    ("C", "C"),
    ("D", "D"),

    )






designation_name = (
    ("Branch Manager", "Branch Manager"),
    ("Teller", "Teller"),
    ("Assistent", "Assistent"),

    )



class Employee_info(models.Model):
    #Bank_name=models.CharField(max_length=50,null=True,blank=True)
    Branch_name=models.CharField(max_length=50,null=True,blank=True)
    Bank=models.ForeignKey(Bank,blank=True, null=True,on_delete=models.CASCADE)
    Branch_code=models.CharField(max_length=50,null=True,blank=True)
    Cluster_head=models.CharField(max_length=50,null=True,blank=True)
    Team_leader=models.CharField(max_length=50,null=True,blank=True)
    Emp_id=models.CharField(max_length=50,null=True,blank=True)
    Emp_name=models.CharField(max_length=50,null=True,blank=True)
    Phone_no=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    designation = models.CharField(max_length=50,null=True,blank=True,choices =designation_name)
    grade=models.CharField(blank=True,null=True,choices =grade,max_length=10)
    CTC=models.CharField(max_length=10,null=True,blank=True)
    remarks = models.TextField(blank=True, null=True)
    State = models.ForeignKey(State,blank=True, null=True,on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)
    Location=models.CharField(max_length=50,null=True,blank=True)
    Alternative_Phone_no=models.CharField(max_length=50,null=True,blank=True)

    City_name=models.CharField(blank=True,null=True,max_length=10)
    District=models.CharField(blank=True,null=True,max_length=10)







