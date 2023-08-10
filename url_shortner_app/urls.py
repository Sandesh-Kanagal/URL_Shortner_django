from django.urls import path
from .views import ShortenURLView, RedirectShortURLView

app_name = 'shortener'
urlpatterns = [
    path('', ShortenURLView.as_view(), name='home'),
    path('<str:short_code>/', RedirectShortURLView.as_view(), name='redirect'),
]
