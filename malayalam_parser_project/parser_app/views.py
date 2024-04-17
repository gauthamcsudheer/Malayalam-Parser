from django.shortcuts import render
from django.http import JsonResponse
import spacy
from textblob import TextBlob

def home(request):
    return render(request, 'home.html')

def extract_entities_and_pos_and_sentiment(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    pos_tags = [(token.text, token.pos_) for token in doc]
    # Perform sentiment analysis using TextBlob
    sentiment = TextBlob(text).sentiment.polarity
    sentiment_label = "Positive" if sentiment > 0 else "Neutral" if sentiment == 0 else "Negative"
    return entities, pos_tags, sentiment_label

def parse_text(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        text = request.POST.get('text', '')
        entities, pos_tags, sentiment = extract_entities_and_pos_and_sentiment(text)
        print(entities)
        print(pos_tags)
        print(sentiment)
        return JsonResponse({'entities': entities, 'pos_tags': pos_tags, 'sentiment': sentiment})
    else:
        return JsonResponse({'error': 'Invalid request'})