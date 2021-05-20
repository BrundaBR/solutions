
def makeaberivation(s,n):
	st=s[0]+str(n-2)+s[-1]
	return st

def checklength(s):
	n=len(s)
	if n>10:
		x=makeaberivation(s,n)
		return (x)
	else:
		return s

T=int(input())
for _ in range(T):
	string=input()
	
	print(checklength(string))