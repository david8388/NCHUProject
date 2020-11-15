import ijson
import json

f = open("./jsonJieba-tran.json")

questions = ijson.items(f, 'item')
answers = []
dictionary = {}
space = ' '

for question in list(questions):
    tokens = question['content'].split('/')
    result = [token for token in tokens if token != '' and token.find('n') != -1]
    for token in result:
        tokenWithoutPOS = token[:token.find(space)]
        if tokenWithoutPOS not in dictionary:
            dictionary[tokenWithoutPOS] = [question['id']]
        elif tokenWithoutPOS in dictionary and question['id'] not in dictionary[tokenWithoutPOS]:
            dictionary[tokenWithoutPOS].append(question['id'])

with open('./dictionary.json', 'w') as fp:
    json.dump(dictionary, fp)
