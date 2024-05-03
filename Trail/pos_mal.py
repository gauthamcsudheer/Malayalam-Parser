# This is a simplified example and requires further development

import nltk
from nltk.tag import hmm

# Sample tagged sentences (replace with your actual data)
tagged_sentences = [
    [("അവൻ", "PRP"), ("പോയി", "VERB")],
    [("പുസ്തകം", "NOUN"), ("മേശപ്പുറത്ത്", "ADP"), ("ഉണ്ട്", "VERB")]
]

# Train a Hidden Markov Model tagger
trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(tagged_sentences)

# Tag a new sentence
text = "അവൾ വീട്ടിൽ പോകുന്നു"
tokens = nltk.word_tokenize(text)
tags = tagger.tag(tokens)

print(tags)