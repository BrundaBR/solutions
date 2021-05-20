def bit(a):
	su=0
	for i in a:
		if i=="++X":
			su+=1
			
		elif i=="X++":
			su+=1
			
		elif i=="X--":
			su-=1
		
		elif i=="--X":
			su-=1
			
		else:
			return
	
	return su

T=int(input())
arr=[]#arr=["X++","--X"]
for _ in range(T):
	string=input()
	arr.append(string)

print(bit(arr))
