'''

'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for q in student_marks:
    	if q==query_name:
    		arr=student_marks.get(q)
    		
    		print(format(sum(arr)/3,".2f"))


    	