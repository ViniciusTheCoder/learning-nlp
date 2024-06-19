import spacy 

nlp = spacy.load('en_core_web_sm')

doc = nlp('She ate the pizza')

for token in doc:
    print(token.text, token.pos_) # the model preview the grammatical classes inside my object with .pos method

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text) # head returns the father of each word

# named entities are real world objects that owns a name, like a person, a organization or a country
#doc.ents allows the model to indetify this entities, that returns an iterable of span objects

doc = nlp('Vinícius, from Apple is looking at buying U.K. startup for $1 billion')

for ent in doc.ents:
    print(ent.text, ent.label_)