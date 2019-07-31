import sys
from itertools import islice

data = sys.argv[1]

# h/t https://stackoverflow.com/a/34400112/2402028
with open(data) as D:
    for i, sli in enumerate(iter(lambda:list(islice(D, 20000)), []), 1):
        with open("split_{}.txt".format(i), "w") as f:
            f.write('\t'.join(['canvas', 'id', 'x', 'y', 'w', 'h', 'order', 'content', 'resource_type', 'motivation', 'format', 'language', 'oa_annotation', '\n']))
            f.writelines(sli)
