n = int(input())

#problem 1111
intervals = []
while len(intervals) < n:
    line = input().strip()
    if line == "":
        continue
    start, end = map(int, line.split())
    intervals.append([start, end])

intervals.sort()
result = []
for start, end in intervals:
    if len(result) == 0:
        result.append([start, end])
    elif start <= result[-1][1]:
        result[-1][1] = max(result[-1][1], end)
    else:
        result.append([start, end])
for start, end in result:
    print(start, end)
