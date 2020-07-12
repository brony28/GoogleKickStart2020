t = int(input())
for _ in range(1,t+1):
	n = int(input())
	v = list(map(int,input().split()))
	count = 0    
	if(v[0]>v[1]):
		count = 1
	vmax = v[0]
	for i in range(1,n):
		if(v[i]>vmax):
			vmax = v[i]
			if(v[i]==v[n-1]):
				count+=1
				# print("Count: ",i,count)
				break
			else:
				if(v[i]>v[i+1]):
					count+=1
					# print("Count: ",i,count)
	print("Case #{}: {}".format(_,count))
        

