import os
import re
from pprint import pprint
from collections import defaultdict
from queue import Queue

final = defaultdict(lambda: defaultdict())
all_files = list()
# adj_list = defaultdict(lambda: defaultdict())
msg = ''

class Node:
    def __init__(self, down_rev, filename, rev) -> None:
        self.down_rev = down_rev
        self.rev = rev
        self.filename = filename

def parser():
    all_data = list()
    
    # read the files and store in string.
    root_dir = 'migration_data_test'
    for root, dirs, files in os.walk('./{}'.format(root_dir)):  
        for filename in files:
            f = dict()
            file_data_str = open(root_dir+'/'+filename).read()
            rev, down_rev = get_revision_str(file_data_str)
            f['rev'] = [rev]
            f['down_rev'] = down_rev
            f['filename'] = filename
            final[down_rev] = f
            all_files.append(filename)


def get_revision_str(f_data):
    m = re.match(r".*?# revision identifiers.*?revision = \'(.*?)\'.*down_revision =(.*?)branch_labels", f_data,re.M|re.S)
    if m:
        d_rev = m.group(2)
        d_rev = re.sub('\s+',' ',d_rev)
        d_rev = re.sub('\'','',d_rev)
        d_rev = re.sub(' ','',d_rev)
    else:
        print('no match!!!!!')
    return(m.group(1), d_rev)

def find_path():
    visited = {}
    level = {}
    parent = {}
    bfs_traversal_output = []
    bfs_traversal_rev_output = []
    queue = Queue()

    for node in final.keys():
        visited[node] = False
        level[node] = -1 #inf
        parent[node] = None

    s = 'None'
    visited[s] = True
    parent[s] = ''
    level[s] = 0
    queue.put(s)

    while not queue.empty():
        u = queue.get()
        bfs_traversal_output.append(u)

        for v in final[u]['rev']:
            bfs_traversal_rev_output.append(v)
            if v in final.keys():
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    level[v] = level[u] + 1
                    queue.put(v)
            else:
                pass
    msg = 'Migration files would be applied in below sequence \n'
    visited_files = []
    for i,path in enumerate(bfs_traversal_output):
        visited_files.append(final[path]['filename'])
        '''Migration files would be applied in below sequence
            a(file1.py) -> b(file2.py) -> c(file4.py) -> d(file3.py)'''
        msg += bfs_traversal_rev_output[i] + '(' + final[path]['filename'] + ') -> ' 
    msg = msg[:-4]
    visited_nodes = final.keys()
    pprint(all_files)
    pprint(visited_files)
    non_visited_files = list(set(all_files) - set(visited_files))
    msg += '\nNon visited File/s ::{}'.format(non_visited_files)
    print(msg)
       

parser()
find_path()
