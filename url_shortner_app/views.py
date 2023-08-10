from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import ShortenedURL
import random
import string

def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))  
    return short_code

class ShortenURLView(View):
    def get(self, request):
        return render(request, 'shortener/home.html')

    def post(self, request):
        original_url = request.POST.get('original_url')
        if original_url:
            short_code = generate_short_code()  
            ShortenedURL.objects.create(original_url=original_url, short_code=short_code)
            short_url = request.build_absolute_uri('/') + short_code
            return render(request, 'shortener/home.html', {'short_url': short_url})
        return redirect('shortener:home')

class RedirectShortURLView(View):
    def get(self, request, short_code):
        shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
        return redirect(shortened_url.original_url)

