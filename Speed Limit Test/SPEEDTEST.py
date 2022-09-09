# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    ali=a/b
    bob=c/d
    if ali>bob:
        print("Alice")
    elif bob>ali:
        print("Bob")
    else:
        print("Equal")