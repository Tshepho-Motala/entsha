from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title

class Delphius_Employee(models.Model):
    fullname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    id_no = models.CharField(max_length=13, null=True)
    emp_code = models.CharField(max_length=200, null=True)
    position = models.ForeignKey(Position,on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Emp_Fname, self.emp_code

class Status(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title

class Employee(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
       return self.name


class Lead(models.Model):
    site = models.CharField(max_length=200, null=True)
    cont_person = models.CharField(max_length=200, null=True)
    cont_no = models.CharField(max_length=13, null=True)
    address = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    status = models.ForeignKey(Status,on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE, null=True)
    started = models.DateTimeField(null=True)
    expected = models.DateTimeField(null=True)
    verified = models.DateTimeField(null=True)
    action = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.site



class Operator(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
       return self.name 

class Duration(models.Model):
    time_frame = models.CharField(max_length=250, null=True)

    def __str__(self):
       return self.time_frame 

class Participation(models.Model):
    rating = models.CharField(max_length=250, null=True)

    def __str__(self):
       return self.rating 

class public_participation(models.Model):
    title = models.CharField(max_length=250, null=True)

    def __str__(self):
       return self.title 

class municipal_approval(models.Model):
    title = models.CharField(max_length=250, null=True)

    def __str__(self):
       return self.title 

class Del_connect_Interest(models.Model):
    title = models.CharField(max_length=250, null=True)

    def __str__(self):
       return self.title 

class solution_shareable(models.Model):
    title = models.CharField(max_length=250, null=True)

    def __str__(self):
       return self.title 


class Delphius_interest(models.Model):
    site_name = models.CharField(max_length=200, null=True)
    cont_person = models.CharField(max_length=200, null=True)
    cont_no = models.CharField(max_length=13, null=True)
    address = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)
    solution_type = models.CharField(max_length=200, null=True)
    est_duration = models.CharField(max_length=200, null=True)
    p_participation = models.ForeignKey(public_participation,on_delete=models.CASCADE, null=True)
    participation = models.ForeignKey(Participation,on_delete=models.CASCADE, null=True)
    municipal_appr = models.ForeignKey(municipal_approval,on_delete=models.CASCADE, null=True)
    est_municipal = models.CharField(max_length=200, null=True)
    est_power_conn = models.CharField(max_length=200, null=True)
    dusk_dawn = models.ForeignKey(Duration,on_delete=models.CASCADE, null=True)
    delconn_interest = models.ForeignKey(Del_connect_Interest,on_delete=models.CASCADE, null=True)
    solution_sh = models.ForeignKey(solution_shareable,on_delete=models.CASCADE, null=True)
    est_solu_cost = models.CharField(max_length=200, null=True)
    operator_interest = models.ForeignKey(Operator,on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

