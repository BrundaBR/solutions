def sum_of_array(arr):
	sum=0
	for i in arr:
		sum+=i
	return sum





arr=list(map(int,input().split()))
print(sum_of_array(arr))