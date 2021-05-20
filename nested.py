
arr=[]
all_val=[]
name_a=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        all_val.append(score)
        arr.append([name,score])
    x=sorted(all_val)
    y=min(x)
    while y in x:
        x.remove(y)
    min_a=x[0]
    for i in arr:
        if i[1]==min_a:
            name_a.append(i[0])
    name_a.sort()
    print("\n".join(name_a))   
