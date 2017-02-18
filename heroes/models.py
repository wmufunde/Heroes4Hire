from django.db import models
from django.conf import settings


class Hero(models.Model):
    codename = models.CharField(max_length = 30)
    profilePic = models.ImageField(blank=True, ) #blank makes this optional
    user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True
)
    
    def __str__(self):
        return str(self.codename)
    
class Stats(models.Model):
    heroID = models.ForeignKey('Hero')
    height = models.CharField(max_length = 10)
    weight = models.CharField(max_length = 10)
    STATS_CHOICES = (
    ('1', 'Extremely Low'),
    ('2', 'Very Low'),
    ('3', 'Low'),
    ('4', 'Average'),
    ('5', 'Good'),
    ('6', 'Above Average'),
    ('7', 'High'),
    ('8', 'Very High'),
    ('9', 'Super Human'),
    ('10', 'Above and Beyond'))
    powers = models.TextField(default="Please add powers")
    intelligence = models.CharField(max_length = 5, choices = STATS_CHOICES)
    durability = models.CharField(max_length = 5, choices = STATS_CHOICES)
    strength = models.CharField(max_length = 5, choices = STATS_CHOICES)
    speed = models.CharField(max_length = 5, choices = STATS_CHOICES)
    
    def __str__(self):
        return str(self.heroID)
        
class Team(models.Model):
    name = models.CharField(max_length = 25)
    leader = models.CharField(max_length = 25)
    address = models.TextField(default="Please Add Address")
    description = models.TextField(default="Please Add Description")
    members = models.TextField(default="Please Add Members")
    
    def __str__(self):
        return str(self.name)

        
class Alias(models.Model):
    heroID = models.ForeignKey('Hero')
    firstName = models.CharField(max_length = 25)
    surname = models.CharField(max_length = 25)
    formerCodeNames = models.TextField(max_length = 25, default="Please Add Former Codenames")
    occupation = models.CharField(max_length = 30)
    address = models.TextField(default="Please Add Address")
    citizenship = models.CharField(max_length = 40)
    species = models.CharField(max_length = 40)
        
    def __str__(self):
        return str(self.firstName, self.surname)


        