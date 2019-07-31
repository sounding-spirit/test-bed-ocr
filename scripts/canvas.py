import sys
import requests
import json

file_list = sys.argv[1]
dir = sys.argv[2]

print ','.join(['manifest',
                'IIIF_IMAGE_SERVER_BASE',
                'id',
                'label',
                'pid',
                'summary',
                'position',
                'height',
                'width',])
                #'is starting page'])

files = open(file_list, 'rU').readlines()
for file in files:
    filename = file.rstrip('\n')
    url = 'http://images.readux.ecds.emory.edu/cantaloupe/iiif/2/' + dir + '_' + filename + '/info.json'
    data = requests.get(url).text
    data = json.loads(data)
    pid = dir + '_' + filename
    position = files.index(file) + 1
    height = data['height']
    width = data['width']
    image_server = 'https://images.readux.ecds.emory.edu:8443/cantaloupe/iiif/2'
    manifest = dir # need to enter dir on command line without a slash
    if position == 1:
        label = 'cover'
        is_starting_page = '1' # importer not yet set up to accept this
    else:
        label = 'canvas ' + str(position)
        is_starting_page = '0' # importer not yet set up to accept this
    print ','.join([manifest,
                    image_server,
                    '',
                    label,
                    pid,
                    '',
                    str(position),
                    str(height),
                    str(width)])
