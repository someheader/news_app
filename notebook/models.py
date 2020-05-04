from django.db import models

# Create your models here.
class ContactType(models.Model):
    contact_type = models.CharField(max_length=100)

    def __str__(self):
        return self.contact_type

class Contact(models.Model):
    c_type = models.ForeignKey(ContactType, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=100)
    register_date = models.DateTimeField('date added')

    def __str__(self):
        return self.contact_name

        