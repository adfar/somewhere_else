from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Review(models.Model):
    business_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="Rating must be at least 1"),
            MaxValueValidator(10, message="Rating cannot be higher than 10")
        ]
    )
    pros = models.TextField(
        help_text="What did you love about this business?"
    )
    cons = models.TextField(
        help_text="What could be improved?"
    )
    review_text = models.TextField(
        help_text="Your detailed review"
    )
    link = models.URLField(
        max_length=255,
        help_text="Link to the business website",
        blank=True  # Makes this field optional
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.business_name} ({self.rating}/10)"

    class Meta:
        ordering = ['-created_at']  # Show newest reviews first