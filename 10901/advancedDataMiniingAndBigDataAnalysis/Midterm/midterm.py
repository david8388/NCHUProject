import jieba
import jieba.analyse
import json
import numpy as np

jieba.set_dictionary('/content/drive/My Drive/Colab Notebooks/dict.txt.big.txt')

# get the dictionary.json after doing preprocessing.py
with open('/content/drive/My Drive/Colab Notebooks/dictionary.json', 'r') as fp:
    dictionary = json.load(fp)

# Provided by Professor
with open('/content/drive/My Drive/Colab Notebooks/Questions_with_Ans.json', 'r') as fp:
    questions = json.load(fp)

answers = []
for question in list(questions):
    keys = jieba.analyse.extract_tags(question['Question'], topK=5, withWeight=False,
                                      allowPOS=('n', 'nrfg', 'nrt', 'nt', 'nz', 'ns', 'nr'))

    ids = []
    print('Question: {}\n, ids: {}\n, Keys: {}\n'.format(question['Question'], ids, keys))
    for key in keys:
        ids += [0] if dictionary.get(key) is None else dictionary.get(key)
    answerForA = len(set(ids) & set(dictionary[question['A']])) if dictionary.get(question['A']) is not None else 0
    answerForB = len(set(ids) & set(dictionary[question['B']])) if dictionary.get(question['B']) is not None else 0
    answerForC = len(set(ids) & set(dictionary[question['C']])) if dictionary.get(question['C']) is not None else 0
    answerMapping = {'A': answerForA, 'B': answerForB, 'C': answerForC}
    answer = max(answerMapping, key=lambda k: answerMapping[k])
    answers.append(answer)


def getJsonList():
    return json.dumps(answers)


print(getJsonList())

print(np.array(answers) == np.array(
    ["B", "C", "B", "A", "C", "A", "A", "C", "B", "B", "A", "C", "C", "B", "A", "B", "A", "C", "B", "B", "C", "A", "C",
     "A", "A", "C", "B", "C", "A", "B", "C", "A", "C", "C", "A", "B", "A", "C", "B", "A", "B", "C", "A", "B", "A", "C",
     "A", "B", "A", "C", "B", "B", "B", "C", "C", "B", "B", "B", "B", "B", "B", "B", "B", "C", "C", "C", "B", "C", "C",
     "A", "B", "C", "B", "C", "B", "B", "B", "A", "B", "C", "A", "A", "B", "A", "C", "B", "B", "C", "A", "C", "B", "C",
     "A", "A", "B", "A", "A", "C", "B", "C", "C", "A", "B", "B", "A", "A", "C", "B", "B", "A", "C", "B", "B", "B", "A",
     "A", "A", "C", "B", "A", "B", "B", "A", "C", "C", "A", "B", "C", "B", "A", "A", "B", "B", "C", "C", "B", "A", "B",
     "C", "", "A", "C", "A", "A", "B", "C", "B", "A", "A", "C", "A", "A", "B", "A", "B", "A", "C", "B", "C", "A", "A",
     "B", "A", "C", "A", "A", "B", "A", "C", "A", "C", "C", "A", "B", "A", "C", "B", "C", "A", "B", "A", "C", "B", "A",
     "C", "A", "B", "A", "B", "B", "B", "C", "C", "A", "A", "B", "B", "B", "B", "B"]
))
