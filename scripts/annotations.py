import sys
import os
import glob
from bs4 import BeautifulSoup

dir = sys.argv[1]
pid_prefix = sys.argv[2]
language = sys.argv[3]
image_ext = sys.argv[4]

dirlist = []
dirlist = sorted(glob.glob(os.path.join(dir, '*.xml')))

print '\t'.join(['canvas', 'id', 'x', 'y', 'w', 'h', 'order', 'content', 'resource_type', 'motivation', 'format', 'language', 'oa_annotation'])

for file in dirlist:
    filename = os.path.basename(file)
    text =  open(file, 'rU').read()
    soup = BeautifulSoup(text, 'lxml')
    strings = soup.find_all('string')
    for string in strings:
        x = string['hpos']
        y = string['vpos']
        w = string['width']
        h = string['height']
        order = strings.index(string) + 1
        content = string['content']
        resource_type = 'ocr'
        motivation = 'painting'
        format = 'plain text'
        canvas = pid_prefix + '_' + filename.rstrip('.xml') + image_ext
        oa_annotation = '{"annotatedBy": {"name": "ocr"}}'
        if content == '':
            pass
        else:
            print '\t'.join([canvas.encode('utf8'),
                            '', # id will be fillled in by system
                            x.encode('utf8'),
                            y.encode('utf8'),
                            w.encode('utf8'),
                            h.encode('utf8'),
                            str(order).encode('utf8'),
                            content.encode('utf8'),
                            resource_type.encode('utf8'),
                            motivation.encode('utf8'),
                            format.encode('utf8'),
                            language.encode('utf8'),
                            oa_annotation.encode('utf8')])

with open('annotation_report.txt', 'w') as outfile:
    outfile.write('filename' + '\t' + 'annotation count' + '\n')
    for file in dirlist:
        filename = os.path.basename(file)
        text =  open(file, 'rU').read()
        soup = BeautifulSoup(text, 'lxml')
        strings = soup.find_all('string')
        count = len(strings)
        outfile.write(filename + '\t' + str(count) + '\n')
    outfile.close()
