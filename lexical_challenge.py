#lexical attribute challenge
# challenge description: from an phrase in portuguese, check if there are number algarisms at the token, if it has, you have to iterate the netx token

import spacy

nlp = spacy.blank('pt')

doc = nlp('Em 1990, mais de 60% da população da Ásia Oriental estava em situação de extrema pobreza.'
    'Agora, menos de 4% está nessa situação.')

for token in doc:
    if token.like_num:
        next_token = doc[token.i + 1]
        if next_token.text == '%':
            print('Percentuais encontrados: ', token.text)
