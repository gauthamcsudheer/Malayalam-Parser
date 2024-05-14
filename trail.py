import spacy
from spacy.language import Language
from spacy.tokens import Doc

# Load a spaCy language model
nlp = spacy.blank("en")

# Define a custom POS tagger component using unsupervised learning
@Language.factory("custom_pos_tagger")
def create_custom_pos_tagger(nlp, name):
    return UnsupervisedPOSTagger()

class UnsupervisedPOSTagger:
    def __call__(self, doc):
        for token in doc:
            # Check token's suffix to determine its POS tag
            if token.text.endswith(('s', 'es', 'ed', 'ing')):
                token.tag_ = 'VERB'
            elif token.text.endswith(('ly')):
                token.tag_ = 'ADV'
            elif token.text.endswith(('able', 'ible')):
                token.tag_ = 'ADJ'
            elif token.text.lower() in ('and', 'but', 'or'):
                token.tag_ = 'CCONJ'
            elif token.text.lower() in ('a', 'an', 'the'):
                token.tag_ = 'DET'
            elif token.text.lower() in ('in', 'on', 'at', 'over', 'under', 'between', 'among', 'around'):
                token.tag_ = 'PREP'    
            elif token.text.lower() in ('i', 'you', 'he', 'she', 'it', 'we', 'they'):
                token.tag_ = 'PRON'
            else:
                token.tag_ = 'NOUN'
        return doc

# Add the custom POS tagger component to the pipeline
nlp.add_pipe("custom_pos_tagger")

# Example text
text = "I was watching the cat that was jumping around."

# Process the text with the pipeline
doc = nlp(text)

# Print tokens with their POS tags
for token in doc:
    print(token.text, token.tag_)
