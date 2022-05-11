from collections import defaultdict

a = [1,1,1,1,1,2,2,2,3,4,5,7,8,99,0,0,3,5,7,9,0,5,4,3,3,2,2,3,3,33]
d = defaultdict(int)
final = list()
for i in a:
    d[i] += 1
for k,v in d.items():
    if d[k] == 1:
        final.append(k)

print(d)
print(final)


