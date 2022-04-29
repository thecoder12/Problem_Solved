import os
import re
from pprint import pprint
from collections import defaultdict
from queue import Queue

final = defaultdict(lambda: defaultdict())
all_obj = list()
adj_list = defaultdict(lambda: defaultdict())
ss = ''

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
            # pprint(final)
            # exit()
            # final[filename]['rev'] = rev
            # final[filename]['down_rev'] = down_rev
            # adj_list = final
            # n = Node(down_rev, filename, rev)
            # print(n.__dict__)
            # all_obj.append(n)
            # exit()


def get_revision_str(f_data):
    # print(f_data)
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
    # pprint(final)
    # exit()

    for node in final.keys():
        # print(node)
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
            # print(v)
            bfs_traversal_rev_output.append(v)
            if v in final.keys():
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    level[v] = level[u] + 1
                    queue.put(v)
            else:
                pass
    # print(bfs_traversal_output)
    ss = 'Migration files would be applied in below sequence \n'
    for i,path in enumerate(bfs_traversal_output):
        # print(final[path]['filename'])
        '''Migration files would be applied in below sequence
            a(file1.py) -> b(file2.py) -> c(file4.py) -> d(file3.py)'''
        ss += bfs_traversal_rev_output[i] + '(' + final[path]['filename'] + ') -> ' 
    ss = ss[:-4]
    print(ss)
       

parser()
# pprint(final)
# pprint(all_obj)
find_path()
