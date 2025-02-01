from django.shortcuts import render
from .models import Review

def reviews_list(request):
    reviews = Review.objects.all().order_by('-rating')  # Highest rated first
    return render(request, 'reviews_list.html', {'reviews': reviews})
