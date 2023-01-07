from django.db import models


class Skills(models.Model):
    skill = models.CharField(max_length=20)


class CareersList(models.Model):
    company = models.CharField(max_length=20)
    job = models.CharField(max_length=20)


class Profile(models.Model):
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
    careers_list = models.ForeignKey(CareersList, on_delete=models.CASCADE)
    careers_text = models.TextField()
    hobbies = models.TextField()
