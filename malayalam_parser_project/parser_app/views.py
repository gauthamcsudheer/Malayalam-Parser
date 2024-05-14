import csv
import spacy
from textblob import TextBlob
from django.http import JsonResponse
from django.shortcuts import render
from deep_translator import GoogleTranslator
from difflib import SequenceMatcher

def home(request):
    return render(request, 'home.html')

def explore(request):
    return render(request, 'explore.html')

def pos_tag_detail(request, pos_tag):
    # Render the respective POS tag page
    return render(request, f'{pos_tag}.html')


def extract_entities_and_pos_and_sentiment(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    pos_tags = [(token.text, token.pos_) for token in doc]
    # Perform sentiment analysis using TextBlob
    sentiment = TextBlob(text).sentiment.polarity
    print(sentiment)
    sentiment_label = "Positive" if sentiment > 0 else "Neutral" if sentiment == 0 else "Negative"
    return entities, pos_tags, sentiment_label, text

def write_to_csv(data, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def write_entities_pos_to_csv(sentence, entities, filename):
    entity_tags = ' '.join([f'{entity}/{tag}' for entity, tag in entities])
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([sentence, entity_tags])

def is_malayalam(text):
    # Check if the text contains Malayalam characters
    malayalam_chars = [char for char in text if 0x0D00 <= ord(char) <= 0x0D7F]
    return len(malayalam_chars) > 0

def translate_to_english(text):
    try:
        translated_text = GoogleTranslator(source='malayalam', target='english').translate(text)
        print(f"{text} -> {translated_text}")
        return translated_text
    except Exception as e:
        print("Translation failed:", e)
        return text  # Return the original text if translation fails

def translate_to_malayalam(text):
    try:
        translated_text = GoogleTranslator(source='english', target='malayalam').translate(text)
        print(f"{text} -> {translated_text}")
        return translated_text
    except Exception as e:
        print("Translation failed:", e)
        return text  # Return the original text if translation fails

def translate_entities_and_tokens(entities, tokens):
    translated_entities = [(translate_to_malayalam(entity), label) for entity, label in entities]
    translated_tokens = [(translate_to_malayalam(token), pos) for token, pos in tokens]
    return translated_entities, translated_tokens

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def filter_translated_tokens(original_malayalam_text, translated_tokens, resemblance_threshold=0.3):
    filtered_tokens = []
    for token, pos in translated_tokens:
        if token is not None:
            found_similar = False
            for original_word in original_malayalam_text.split():
                resemblance_score = similar(original_word, token)
                print(f'{original_word} - {token} -> {resemblance_score}')
                if resemblance_score is not None and resemblance_score >= resemblance_threshold:
                    print(f'{original_word} <--> {token}, Similarity: {resemblance_score}')
                    found_similar = True
                    break
            if found_similar:
                filtered_tokens.append((token, pos))
    return filtered_tokens

# def open_and_parse_csv(input_filename):
#     with open(input_filename, 'r', newline='', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             sentence = row[0]
#             parse_text(sentence)

def parse_text(request):

    language = 0

    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        text = request.POST.get('text', '')
     
        # Check if the text is in Malayalam
        if is_malayalam(text):
            language = 1
            original_malayalam_text = text  # Save the original Malayalam text
            text = translate_to_english(text)

        entities, pos_tags, sentiment, sentence = extract_entities_and_pos_and_sentiment(text)

        if language:
            # Translate entities and tokens back to Malayalam
            translated_entities, translated_tokens = translate_entities_and_tokens(entities, pos_tags)

            # Filter translated tokens using original Malayalam text
            filtered_translated_tokens = filter_translated_tokens(original_malayalam_text, translated_tokens)

            print(translated_entities)
            print(filtered_translated_tokens)

            # Write entities to CSV file
            write_entities_pos_to_csv(original_malayalam_text, translated_entities, './static/entities.csv')
            # Write POS tags to CSV file
            write_entities_pos_to_csv(original_malayalam_text, filtered_translated_tokens, './static/pos_tags.csv')
            # Write sentiment and sentence to CSV file
            with open('./static/sentiment.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([original_malayalam_text, sentiment])

            return JsonResponse({'entities': translated_entities, 'pos_tags': filtered_translated_tokens, 'sentiment': sentiment})
        
        else:
            # Write entities to CSV file
            write_entities_pos_to_csv(text, entities, './static/entities.csv')
            # Write POS tags to CSV file
            write_entities_pos_to_csv(text, pos_tags, './static/pos_tags.csv')
            # Write sentiment and sentence to CSV file
            with open('./static/sentiment.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([sentence, sentiment])
            return JsonResponse({'entities': entities, 'pos_tags': pos_tags, 'sentiment': sentiment})
    else:
        return JsonResponse({'error': 'Invalid request'})

# open_and_parse_csv('./static/input.csv')
