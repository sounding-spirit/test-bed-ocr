import sys
import os
import glob
from bs4 import BeautifulSoup

hocr_dir = sys.argv[1]
annotation_dir = sys.argv[2]

dirlist = []
dirlist = sorted(glob.glob(os.path.join(hocr_dir, '*.hocr')))


for file in dirlist:
    text =  open(file, 'rU').read()
    soup = BeautifulSoup(text)

    out = os.path.join(annotation_dir, os.path.basename(file).rstrip('.hocr')+ '.tsv')
    with open(out, 'w') as outfile:
        outfile.write('\t'.join(['content', 'x', 'y', 'w', 'h', '\n']))
        '''
        Example:
        <span class='ocrx_word' id='word_1_4' title='bbox 913 180 1155 224; x_wconf 96'>RUDIMENTS</span>
        '''
        for span in soup.find_all('span', {'class': 'ocrx_word'}):
            coord_data = span['title']
            x = int(coord_data.split(' ')[1])
            y = int(coord_data.split(' ')[2])
            lower_x = int(coord_data.split(' ')[3])
            lower_y = int(coord_data.split(' ')[4].rstrip(';'))
            w = abs(lower_x - x)
            h = abs(lower_y - y)
            content = span.string.encode('utf8')
            if content == '' or content == '"':
                pass
            else:
                outfile.write('\t'.join([content, str(x), str(y), str(w), str(h), '\n']))
