import uuid
from django.db import models
from app.client.models import Client
from app.package.models import Package



class Gallery(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False)
    link = models.CharField(max_length=255, blank=False, null=False)
    link_pass = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name