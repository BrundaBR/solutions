def string_fun(s):
	vowels=["A","a","O","o","Y",
	"y","E","e","U","u","i","I"]
	res=[]
	for i in s:
		if i not in vowels:

			res.append(".")
			if i==i.upper():
				res.append(i.lower())
			else:
				res.append(i)

	return "".join(res)

string=input()
print(string_fun(string))