# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    print(a+((b-c)*d))