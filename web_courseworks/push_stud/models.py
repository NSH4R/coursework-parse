from django.db import models


class Groups(models.Model):
    group_name = models.CharField(max_length=10)


class Students(models.Model):
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    student_url = models.CharField(max_length=100)
    student_first_name = models.CharField(max_length=20)
    student_name = models.CharField(max_length=20)
    student_second_name = models.CharField(max_length=20)


class Portfolio(models.Model):
    student_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
