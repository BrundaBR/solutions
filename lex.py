
def compare(s1,s2):
	if s1==s2:
		return 0
	elif s1<s2:
		return -1
	else:
		return 1
	





str1=input().lower()
str2=input().lower()
print(compare(str1,str2))