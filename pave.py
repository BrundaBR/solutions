from math import ceil
def pave(l):
	n=l[0]
	m=l[1]
	a=l[-1]
	row=n/a
	col=m/a
	x=ceil(row)
	y=ceil(col)
	return x*y






lis=list(map(int,input().split()))
print(pave(lis))