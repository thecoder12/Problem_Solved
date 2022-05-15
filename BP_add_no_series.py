'''
N=10
'''
N=7
sum = 0
for i in range(N+1):
    if (i%5) !=0:
        if (i%7) !=0:
            print(i)
            sum += i
print(sum)
