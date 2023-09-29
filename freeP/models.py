from django.db import models
from django.contrib.auth.models import User
class Days(models.Model):
    Day=models.CharField()
    def __str__(self):
        return self.Day

class Details(models.Model):
    Name=models.ForeignKey(User, on_delete=models.CASCADE,related_name="day1")
    Day1=models.ForeignKey(Days, on_delete=models.CASCADE,related_name="day2")
    Day2=models.ForeignKey(Days, on_delete=models.CASCADE,related_name="day3")
    Day3=models.ForeignKey(Days, on_delete=models.CASCADE,related_name="day4")
    Messages=models.TextField(max_length=100)
    Reserve_Points=models.IntegerField()
    def __str__(self):
        return self.Name.username

class Period(models.Model):
    Name=models.ForeignKey(User, on_delete=models.CASCADE,related_name="day2")
    Day=models.ForeignKey(Days, on_delete=models.CASCADE,related_name="day5")
    Time=models.TimeField()
    Free=models.BooleanField()
    Free_Period_Taken_By=models.ForeignKey(User, on_delete=models.CASCADE,related_name="day6")
    def __str__(self):
        return str(self.Name.username)+'_'+str(self.Day.Day)