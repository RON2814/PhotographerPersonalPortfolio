from django.db import models

class PortfolioProject(models.Model):
    CATEGORY_CHOICES = [
        ('fashion', 'Fashion'),
        ('nature', 'Nature'),
        ('wedding', 'Wedding'),
        ('product', 'Product'),
        ('studio', 'Studio'),
        ('sports', 'Sports'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='fashion')
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when a project is created
    updated_at = models.DateTimeField(auto_now=True)      # Automatically set whenever a project is updated

    def __str__(self):
        return self.title
