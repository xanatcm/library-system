import uuid
from django.db import models

# Create your models here.


class Library(models.Model):
    name = models.CharField(max_length=250)
    adress = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    @property
    def name_adress(self):
        return f"{self.name} | {self.adress}"


class Rack(models.Model):
    number = models.IntegerField(unique=True)
    uuid = models.UUIDField(default=uuid.uuid4())
    place = models.ForeignKey(Library, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.place} | {self.number}"

    @property
    def name_uuid(self) -> dict:
        return {
            "number": self.number,
            "uuid": self.uuid
        }
