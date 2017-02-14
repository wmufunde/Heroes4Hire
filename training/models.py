from django.db import models

# Create your models here.
from heroes.models import Hero


class Trainer(models.Model):
    firstName = models.CharField(max_length = 25)
    surname = models.CharField(max_length = 25)
    gender = models.CharField(max_length = 15)
    address = models.TextField(default="Please Add Address")
    citizenship = models.CharField(max_length = 40)
    
    def __str__(self):
        return '%s %s' % (self.firstName, self.surname)
    
class Room(models.Model):
    roomName = models.CharField(max_length = 30)
    
    def __str__(self):
        return str(self.roomName)
    
class ClassTraining(models.Model):
    TrainerID = models.ForeignKey(Trainer)
    roomID = models.ForeignKey(Room)
    TRAINING_TYPE_CHOICES = (
    ('AC', 'Armed Combat'),
    ('UC', 'Unarmed Combat'),
    ('P', 'Piloting'),
    ('O', 'Other'),
)
    className = models.CharField(max_length= 20)
    typeofClass = models.CharField(max_length = 5, choices = TRAINING_TYPE_CHOICES)
    description = models.TextField(default="Please Add Description")
    
    def __str__(self):
        return '%s %s' %(self.className, self.typeofClass)
    
class Attendance(models.Model):
    heroID = models.ForeignKey(Hero) #initially heroesode
    classID = models.ForeignKey(ClassTraining)
    roomID = models.ForeignKey(Room)
    classDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    
    def __str__(self):
        return str(self.heroID, self.classID, self.roomID)
    
class ReportLog(models.Model):
    classID = models.ForeignKey(ClassTraining)
    heroID = models.ForeignKey(Hero)
    TrainerID = models.ForeignKey(Trainer)
    grade = models.CharField(max_length = 5)
    OUTCOME_CHOICES = (
    ('P', 'Pass'),
    ('F', 'Fail'),
    )
    outcome = models.CharField(max_length = 1, choices = OUTCOME_CHOICES)
    comments = models.TextField()
    
    def __str__(self):
        return '%s %s %s %s' %(self.heroID, self.classID, self.grade, self.outcome)
