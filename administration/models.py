from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=40, help_text="Name", null=False)
    last_name = models.CharField(max_length=40, help_text="Last name", null=False)
    email = models.EmailField(null=False)

    def __str__(self):
        return "{} {} {}".format(self.name, self.last_name, self.email)
