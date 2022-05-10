'''
https://www.geeksforgeeks.org/count-strings-can-formed-using-b-c-given-constraints/
Input : n = 3 
Output : 19 
Below strings follow given constraints:
aaa aab aac aba abc aca acb acc baa
bac bca bcc caa cab cac cba cbc cca ccb 

Input  : n = 4
Output : 39

Given a length n, count the number of strings of length 'n'
that can be made using ‘a’, ‘b’ and ‘c’ with at-most one ‘b’ and two ‘c’s allowed.
a >= 0 ; b<=1 ; c<=2
'''

from itertools import permutations, product
from collections import defaultdict

n = 4
a = 'abc'

def check(a):
    d = defaultdict(int)
    for i in list(a):
        print(i, d)
        d[i] += 1
    if d['b'] <= 1 and d['c'] <= 2:
        return True
    else:
        return False

final = list()
for i in product(a, repeat=n):
    if check(i):
        final.append(i)
print(len(final))
