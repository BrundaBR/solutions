from math import ceil,floor
def domino(l):
	m=l[0]
	n=l[1]
	x=floor((m*n)/2)
	return x

lis=list(map(int,input().split()))
print(domino(lis))