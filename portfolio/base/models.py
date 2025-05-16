from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=20 )
    email = models.EmailField()
    phone_no = models.CharField(max_length=15, blank=False, null=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'message form {self.name} - {self.created_at}'