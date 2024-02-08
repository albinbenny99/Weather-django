from django.db import models
from accounts.models import Account  # Import your custom user model

class Chat(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email}: {self.message}'
