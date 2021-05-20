def qualify(a,k):
	score_boundry=a[k-1]
	su=0
	for i in range(len(a)):
		if a[i]>=score_boundry and a[i]!=0:
			su+=1
		else:
			continue
	return su





q1=list(map(int,input().split(" ")))
arr=list(map(int,input().split(" ")))
print(qualify(arr,q1[1]))