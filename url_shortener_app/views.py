# url_shortener_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ShortenedURL
import random
import string

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def index(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        short_code = generate_short_code()

        # Save the original URL and short code to the database
        ShortenedURL.objects.create(original_url=original_url, short_code=short_code)

        # Build the shortened URL for the response
        base_url = request.build_absolute_uri('/')
        shortened_url = f'{base_url}{short_code}/'

        # Return the shortened URL as a plain text response
        return HttpResponse(shortened_url)

    return render(request, 'index.html')

def redirect_to_original(request, short_code):
    shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
    return redirect(shortened_url.original_url)