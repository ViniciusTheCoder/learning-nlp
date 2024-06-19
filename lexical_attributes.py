import spacy

nlp = spacy.blank('en')

doc = nlp('It costs $5.')

print('Index: ', [token.i for token in doc])
print('Text: ', [token.text for token in doc])

print('is_alpha: ', [token.is_alpha for token in doc]) # check if there are alphanumeric characters
print('is_punct: ', [token.is_punct for token in doc]) # check if there are . , ! : '' ;
print('like_num: ', [token.like_num for token in doc]) # check if there are similar to number


