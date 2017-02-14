from django.db import models

# Create your models here.
from heroes.models import Hero, Team


class Customer(models.Model):
    firstName = models.CharField(max_length = 25)
    surname = models.CharField(max_length = 25)
    gender = models.CharField(max_length = 15, default = 'Please Add Gender')
    address = models.TextField()
    citizenship = models.CharField(max_length = 40)
    
    def __str__(self):
        return '%s %s' % (self.firstName, self.surname)
    
class Mission(models.Model):
    customerID = models.ForeignKey(Customer)
    description = models.TextField()
    locations = models.TextField()
    DIFFICULTY_CHOICES = (
    ('1', 'Very Easy'),
    ('2', 'Easy'),
    ('3', 'Average'),
    ('4', 'Difficult'),
    ('5', 'Very Difficult'),
)
    difficulty = models.CharField(max_length = 5, choices = DIFFICULTY_CHOICES)
    
    def __str__(self):
        return str(self.description)
    
class Report(models.Model):
    missionID = models.ForeignKey(Mission)
    OUTCOME_CHOICES = (
    ('U', 'Unsuccessful'),
    ('S', 'Successful'),
)
    heroID = models.ForeignKey(Hero) #initially heroesode
    outcome = models.CharField(max_length = 5, choices = OUTCOME_CHOICES)
    comments = models.TextField()
    
    def __str__(self):
        return str(self.missionID, self.outcome)


class Status(models.Model):
    heroID = models.ForeignKey(Hero)
    missionID = models.ForeignKey(Mission, null=True, blank=True)
    teamID = models.ForeignKey(Team, blank=True, null=True)

    def __str__(self):
        return str(self.heroID, self.missionID, self.TeamID)
