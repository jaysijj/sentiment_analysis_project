from django.contrib import admin
from django.urls import path
from sentiment_api.views import analyze_sentiment
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('api/analyze_sentiment/', analyze_sentiment, name='analyze_sentiment'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)