from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Complaint(models.Model):

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]

    name = models.CharField(max_length=100)
    message = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='open'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.namez