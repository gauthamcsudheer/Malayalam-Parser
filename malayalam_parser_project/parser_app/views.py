import csv
import spacy
from textblob import TextBlob
from indicnlp.tokenize import indic_tokenize
from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def is_english(text):
    try:
        text.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def extract_entities_and_pos_and_sentiment(text, language):
    if language == 'english':
        nlp = spacy.load("en_core_web_sm")
        tokenizer = spacy.tokenizer.Tokenizer(nlp.vocab)
        doc = tokenizer(text)
        entities = [(entity.text, entity.label_) for entity in doc.ents]
        pos_tags = [(token.text, token.pos_) for token in doc]
        sentiment = TextBlob(text).sentiment.polarity
    elif language == 'malayalam':
        tokenizer = indic_tokenize.trivial_tokenize
        tokens = tokenizer(text)
        # You need to load a Malayalam language model for POS tagging and Named Entity Recognition
        # Replace 'ml_core_news_sm' with the appropriate Malayalam language model
        nlp = spacy.load("xx_sent_ud_sm")
        doc = nlp(" ".join(tokens))
        entities = [(entity.text, entity.label_) for entity in doc.ents]
        pos_tags = [(token.text, token.pos_) for token in doc]
        sentiment = None  # Sentiment analysis for Malayalam text is not straightforward, you may need a different approach
    else:
        entities = []
        pos_tags = []
        sentiment = None
    return entities, pos_tags, sentiment

def write_to_csv(data, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def parse_text(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        text = request.POST.get('text', '')
        language = 'english' if is_english(text) else 'malayalam'
        entities, pos_tags, sentiment = extract_entities_and_pos_and_sentiment(text, language)
        # Write entities to CSV file
        write_to_csv(entities, './static/entities.csv')
        # Write POS tags to CSV file
        write_to_csv(pos_tags, './static/pos_tags.csv')
        # Write sentiment to CSV file
        if sentiment is not None:
            with open('./static/sentiment.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([text, sentiment])
        return JsonResponse({'entities': entities, 'pos_tags': pos_tags, 'sentiment': sentiment})
    else:
        return JsonResponse({'error': 'Invalid request'})
