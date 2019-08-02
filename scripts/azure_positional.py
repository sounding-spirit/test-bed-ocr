import sys
import json
import os
import glob

json_dir = sys.argv[1]
annotation_dir = sys.argv[2]

dirlist = []
dirlist = glob.glob(os.path.join(json_dir, '*.json'))

for file in dirlist:
    with open(file, 'rU') as f:
        data = f.read()
        data = json.loads(data)

        out = os.path.join(annotation_dir, os.path.basename(file).rstrip('.json')+ '.tsv')
        with open(out, 'w') as outfile:
            outfile.write('\t'.join(['content', 'x', 'y', 'w', 'h', '\n']))
            for region in data['regions']:
                for line in region['lines']:
                    for word in line['words']:
                        '''
                        Example
                        "boundingBox": "725,257,246,29",
                        "text": "RUDIMENTS"
                        '''
                        coordinates = word['boundingBox']
                        x = coordinates.split(',')[0]
                        y = coordinates.split(',')[1]
                        w = coordinates.split(',')[2]
                        h = coordinates.split(',')[3]
                        content = word['text'].encode('utf8')

                        if content == '' or content[0] == '"':
                            pass
                        else:
                            outfile.write('\t'.join([content, str(x), str(y), str(w), str(h), '\n']))
