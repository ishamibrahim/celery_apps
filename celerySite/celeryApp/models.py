from django.db import models


class SquareNumber(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "PENDING"),
        ("COMPLETE", "COMPLETE"))
    number = models.IntegerField(null=True)
    square_number = models.IntegerField(null=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="PENDING")
