n=int(input("Enter your input:"))
intervals=[]
for _ in range(n):
    start, end=map(int, input().split())
    intervals.append([start, end])
intervals.sort(key=lambda x:x[0])
merged=[]
for start, end in intervals:
    if not merged or start > merged[-1][1]:
        merged.append([start, end])
    else:
        merged[-1][1]=max(merged[-1][1],end)
for start, end in merged:
    print(start, end)
#test case1
5

4 2 7 1 9

1
output-9
#test case2
4

1 2 3 4
#output-INCORRECT
#test case3
5

-8 -3 -6 -2 -5

2


#output -3
#test case4
5

1 2 3 4 5

3
#output 12
#test case5
6

4 -1 2 1 -5
4

2
#output 3


