import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)

pattern = [{'TEXT': 'iPhone'}, {'TEXT': 'X'}]
matcher.add("IPHONE_PATTERN", [pattern])

doc = nlp('Upcoming iPhone X release date leaked')
matches = matcher(doc)
print(matches) # this print return a tuples list, it brings the expression ID, starting index and ending index
print('Correspondências: ', [doc[start:end].text for match_id, start, end in matches])

for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)

#searching for complex attributes

pattern = [ # here we are lookin for five tokens, a token digit only, three tokens in lowercase and one punct only token
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world"},
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
]

doc = nlp("2018 FIFA World Cup: France won!")

pattern = [ # here we are looking for words that are like love and after them it has to be a noun
    {"LEMMA": "love", "POS": "VERB"},
    {"POS": "NOUN"}
]

doc = nlp("I loved dogs but now I love cats more.")

# OP can have 4 different value operators

# {"OP": "!"}	Denial: matches once
# {"OP": "?"}	Optional: matches 0 or once
# {"OP": "+"}	Matches once or more
# {"OP": "*"}	Mtches 0 or more