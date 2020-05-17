res=[]
from math import sqrt,floor
for r in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))
    C = [sum(li[i:j]) for i in range(len(li)+1) for j in range(i+1,len(li)+1)]
    count=0
    for k in C:
    	sq = sqrt(k)
    	if(sq - floor(sq) == 0):
    		count+=1
    # print(f'Case #{r+1}: {count}')
    res.append(count)
    
for x in range(len(res)):
    print('Case #{}: {}'.format(x + 1, res[x]))

