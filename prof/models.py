from django.db import models


class Profile(models.Model):
    careers_text = models.TextField()
    hobbies = models.TextField()

    def __str__(self):
        return 'jin'


class Skills(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='skills')
    skill = models.CharField(max_length=20)


class CareersList(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='careers_list')
    company = models.CharField(max_length=20)
    job = models.CharField(max_length=20)


class Study(models.Model):
    title = models.CharField(max_length=50)
    comment = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
