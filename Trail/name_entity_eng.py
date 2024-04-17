import spacy

def named_entity_recognition(text):
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")
    
    # Process the text
    doc = nlp(text)
    
    # Extract named entities
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    
    return entities

if __name__ == "__main__":
    # Example text
    text = "Barack Obama was born in Hawaii."
    
    # Perform named entity recognition
    entities = named_entity_recognition(text)
    
    # Print the results
    print(entities)
