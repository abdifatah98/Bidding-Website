from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Auction(models.Model):
    BOOL_CHOICES = ((True, 'Open'), (False, 'Close'))

    ID = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 50)
    Image = models.ImageField(upload_to='images/')
    Description = models.CharField(max_length = 150)
    AuctionEnd = models.DateTimeField()
    Stats = models.BooleanField(choices=BOOL_CHOICES, default = True) #status of auction
    CurrentPrice = models.IntegerField()
    HighestBidder = models.ForeignKey('Accounts',on_delete=models.SET_NULL,blank=True,null = True)

    def __str__(self):
        return self.Name

class Accounts(AbstractUser):
    dateofbirth = models.DateTimeField(default="1998-02-02", null=True, blank=True)
    pass
