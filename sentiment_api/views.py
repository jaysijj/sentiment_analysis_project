from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


nltk.download('vader_lexicon')

# Crie uma instância do SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

@api_view(['POST'])
def analyze_sentiment(request):
    text = request.data.get('text', '')

    # Realize a análise de sentimento usando o SentimentIntensityAnalyzer
    sentiment_score = sia.polarity_scores(text)
    
    # Converta a pontuação em uma categoria de sentimento
    if sentiment_score['compound'] >= 0.05:
        sentiment = 'Positivo'
    elif sentiment_score['compound'] <= -0.05:
        sentiment = 'Negativo'
    else:
        sentiment = 'Neutro'

    return Response({'sentiment': sentiment})