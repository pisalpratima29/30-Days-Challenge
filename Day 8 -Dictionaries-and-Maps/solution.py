# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(input())
dict = dict(input().split(" ") for _ in range(0,n))

for i in range(0,n):
    key = str(input())
    if key in dict.keys():
        print(key+'='+dict[key])
    else:
        print('Not found')
        