from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    agent=models.ForeignKey("Agent",on_delete=models.CASCADE)

    def __str__(self) :
        return f"{self.first_name} {self.last_name}"
    # SOURCE_CHOICES=(
    #     ('YouTube', 'YouTube'),
    #     ('Google', 'Google'),
    #     ('Newsletter', 'Newsletter')
    # )

    # phoned=models.BooleanField(default=False)
    # source=models.CharField(choices=SOURCE_CHOICES, max_length=100)
    # profile_picture=models.ImageField(blank=True,null=True)
    # special_files=models.FileField(blank=True,null=True)

class Agent(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    # as we have these fileds in the abstract user model no need to do this
    # first_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)