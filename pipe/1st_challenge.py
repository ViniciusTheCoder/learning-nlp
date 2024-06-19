import spacy

nlp = spacy.load('pt_core_news_sm')

text = 'Vazou a data de lançamento do novo iPhone X após a Apple revelar a existência de compras antecipadas.'

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)

iphone_x = doc[7:9]

print('Missing entity: ', iphone_x.text)