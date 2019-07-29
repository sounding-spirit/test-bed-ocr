import sys
import json

file = sys.argv[1]

with open(file, 'rU') as f:
    data = f.read()
    data = json.loads(data)

for region in data['regions']:
    for line in region['lines']:
        words = []
        for word in line['words']:
            words.append(word['text'].encode('utf8'))
        print(' '.join(words))
