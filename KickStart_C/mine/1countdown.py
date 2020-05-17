

results=[]
for j in range(int(input())):
	n,k = map(int,input().split())
	A = list(map(int,input().split()))
	    
	val = list(range(k,0,-1))
	count=0
	l=len(A)
	for i in range(l):
		rbk=[]
		if A[i] == k:
			rbk = A[i:i+k]
			if(rbk==val):
				count+=1
# 	print(f"Case #{j+1}: {count}")			    
    results.append(count)

for x in len(results):
    print('Case #{}: {}'.format(x + 1, results[x]))
    