import os
import re
from pprint import pprint
from collections import defaultdict

final = defaultdict(lambda: defaultdict())

def parser():
    all_data = list()
    # read the files and store in string.
    root_dir = 'migration_data_test'
    for root, dirs, files in os.walk('./{}'.format(root_dir)):  
        for filename in files:
            file_data_str = open(root_dir+'/'+filename).read()
            rev, down_rev = get_revision_str(file_data_str)
            final[filename]['rev'] = rev
            final[filename]['down_rev'] = down_rev


def get_revision_str(f_data):
    # print(f_data)
    m = re.match(r".*?# revision identifiers.*?revision = \'(.*?)\'.*down_revision =(.*?)branch_labels", f_data,re.M|re.S)
    if m:
        # print(m.group(0))
        print('------')
        print(m.group(1))
        print('********')
        d_rev = m.group(2)
        d_rev = re.sub('\s+',' ',d_rev)
        d_rev = re.sub('\'','',d_rev)
        d_rev = re.sub(' ','',d_rev)
        print(d_rev)
        print('------')
        # x.replace("\n", "")
    else:
        print('no match!!!!!')
    return(m.group(1), d_rev)



def find_path(graph, start, end, path=[]):
path = path + [start]
if start == end:
    return path
for node in graph[start]['rev']:
    if node not in path:
        newpath = find_path(graph, node, end, path)
        if newpath:
            return newpath

parser()
pprint(final)
find_path(final,'1de5a8c20056_initial_migration_include.py', )
