'''
Paper Cut into Minimum Number of Squares | Set 2
Difficulty Level : Hard
Last Updated : 21 May, 2021
Given a paper of size A x B. Task is to cut the paper into squares of any size. 
Find the minimum number of squares that can be cut from the paper. 

Examples: 
Input  : 36 x 30
Output : 5
Explanation : 3 (squares of size 12x12) + 2 (squares of size 18x18)

Input  : 4 x 5
Output : 5
Explanation : 1 (squares of size 4x4) + 4 (squares of size 1x1)
'''
from collections import defaultdict
large = 3610
small = 30
total_sq = large*small
# print(total_sq)
t_sq = 0
final = defaultdict()

def find_sq(n):
    global large
    if (large % n) == 0:
        rem = large % n
        quo = large//n
        final[n] = quo
        return(t_sq)
    rem = large % n
    quo = large//n
    final[n] = quo
    large = n
    print(rem, quo, large)
    find_sq(rem)


find_sq(min(large, small))
print(final)

sum = 0
#cross-check the code
for side,repeat in final.items():
    print(side,repeat)
    sum += side*side*repeat
    
print('given::{} :: calculated::{}'.format(total_sq, sum))
if sum == total_sq:
    print('all the squares are completed')
else:
    print('something is missing')