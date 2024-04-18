import csv
import spacy
from textblob import TextBlob
from django.http import JsonResponse
from django.shortcuts import render

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
    return entities, pos_tags, sentiment_label, text

def write_to_csv(data, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def parse_text(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        text = request.POST.get('text', '')
        entities, pos_tags, sentiment, sentence = extract_entities_and_pos_and_sentiment(text)
        # Write entities to CSV file
        write_to_csv(entities, './static/entities.csv')
        # Write POS tags to CSV file
        write_to_csv(pos_tags, './static/pos_tags.csv')
        # Write sentiment and sentence to CSV file
        with open('./static/sentiment.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([sentence, sentiment])
        return JsonResponse({'entities': entities, 'pos_tags': pos_tags, 'sentiment': sentiment})
    else:
        return JsonResponse({'error': 'Invalid request'})
