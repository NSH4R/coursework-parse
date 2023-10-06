from django.db import models
import uuid


class Groups(models.Model):
    group_name = models.CharField('Группа',max_length=10)


class Students(models.Model):
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    student_first_name = models.CharField('Фамилия', max_length=20)
    student_name = models.CharField('Имя', max_length=20)
    student_second_name = models.CharField('Отчество', max_length=20)
    students_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Portfolio(models.Model):
    subject = models.TextField(max_length=100)
    title = models.TextField(max_length=250)
    student_uuid = models.ForeignKey(Students, on_delete=models.CASCADE)
