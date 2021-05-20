'''
greedy
3 friends 2 should be sure
n problems

'''





T=int(input())
su=0
for _ in range(T):
	li=list(map(int,input().split(" ")))
	x=sum(li)
	if x>=2:
		su+=1
	else:
		continue
print(su)



