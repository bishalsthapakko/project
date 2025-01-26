from django.db import models

class Storeinstruments(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='store_images/')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
