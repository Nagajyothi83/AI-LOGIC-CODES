s = input().strip()
seen = set()
left = 0
maximum = 0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    length = right - left + 1

    if length > maximum:
        maximum = length
print(maximum)

'''#TEST CASE1
a
1'''
'''#TEST CASE2
aaaaaa
1'''
'''#TEST CASE3
abcdef
6'''
'''#TEST CASE4
aa
1'''

'''#TEST CASE5
abca
3'''



