from django.db import models
from django.core import validators as v
from .validators import validate_name, validate_school_email, validate_combination_format
from subject_app.models import Subject

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null = False, blank = False, validators=[validate_name])
    student_email = models.EmailField(null = False, blank = False, unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(null = False, blank = False, unique=True)
    locker_number = models.IntegerField(default = 110, null = False, blank = False, unique=True, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField( default="12-12-12",null = False, blank = False,max_length=255, validators=[validate_combination_format])
    good_student = models.BooleanField(default=True)
    subjects = models.ManyToManyField(Subject, related_name='students')

    def __str__(self):
        return f'{self.name}-{self.student_email}-{self.locker_combination}'
    
    def locker_reassignment(self, new_combo):
        if new_combo is type(int):
            self.locker_combination = new_combo
        else:
            return 'Locker combination must be an INT'
        self.save()

    def student_status(self, new_status):
        if new_status is type(bool):
            self.good_student = new_status
        else:
            return 'Student status must be a Boolean'
        self.save()

    def add_subject(self, subject_id):
        if self.subjects.count() >= 8:
            raise Exception('This students class schedule is full!')
        else:
            self.subjects.add(subject_id)
            self.save()

    def remove_subject(self, subject_id):
        if self.subjects.count() <= 1:
            raise Exception("This students class schedule is empty!")
        else:
            self.subjects.remove(subject_id)
            self.save()
        
