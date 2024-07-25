from django.db import models
from django.core import validators as v
from .validators import validate_professor_name, validate_subject

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=100, null=False, blank=False, unique=True, validators=[validate_subject])
    professor = models.CharField(null=False, blank=False, max_length=100, validators=[validate_professor_name])
    # many to many relationship created in students model 
    # students = models.manytomanyfield(subjects, relatedname='students')
    
    def __str__(self):
        return f"{self.subject_name} - {self.professor} - {self.students.count()}"

    def add_a_student(self, student_id):
        #how can i use students in this file without creating a circular import
        if self.students.count() < 31:
            self.students.add(student_id)
        else:
            raise Exception("This subject is full!")

    def drop_a_student(self, student_id):
        if self.students.count() > 0:
            self.students.remove(student_id)
        else:
            raise Exception("This subject is empty!")
    

    

