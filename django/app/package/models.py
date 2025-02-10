import uuid
from django.db import models
from app.client.models import Client
from datetime import date



class Plan(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False) #dias
    price = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return self.name


class Package(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    created_at = models.DateField(default=date.today())
    deadline = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.client.name + '_' + self.plan.name + '_' + self.created_at.strftime("%d/%m/%Y") + '_' + self.deadline.strftime("%d/%m/%Y")