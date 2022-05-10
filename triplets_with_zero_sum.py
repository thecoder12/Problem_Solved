#https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/

'''
Input : arr[] = {0, -1, 2, -3, 1}
Output : (0 -1 1), (2 -3 1)

Explanation : The triplets with zero sum are
0 + -1 + 1 = 0 and 2 + -3 + 1 = 0  

Input : arr[] = {1, -2, 1, 0, 5}
Output : 1 -2  1
Explanation : The triplets with zero sum is
1 + -2 + 1 = 0   
'''

arr = [0, -1, 2, -3, 1]
op = [(0,-1,1), (2,-3,1)]


from itertools import permutations, combinations

final = list()
rr_perm = combinations(arr, 3)

for i in rr_perm:
    # print(i)
    if sum(i) == 0 and i not in final:
        final.append(i)
print(final)

'''
(base) Coder_Solver % python3 triplets_with_zero_sum.py
[(0, -1, 1), (2, -3, 1)]
(base) Coder_Solver % 
'''
