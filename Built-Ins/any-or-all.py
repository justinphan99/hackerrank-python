n = int(input())
a = list(input().split())
if all(int(x)>0 for x in a) and any(x ==x[::-1] for x in a):
    print ('True')
else: 
    print('False')