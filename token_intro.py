import spacy

nlp = spacy.blank('en')

doc = nlp('Hello World!')

for token in doc: # this will allow us to iterate for each token in the string
    print(token.text)

token = doc[1] ## here we take only the first token at the iteration
print(token.text)

# now lets take the tokens between 1st and 3rd token, but we'll not get the last one

span = doc[1:3]
print(span.text)