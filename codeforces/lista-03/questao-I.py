diam = int(input())
alt, larg, prof = map(int,input().split())

if (diam > alt or diam > larg or diam > prof):
    print("N")
else:
    print("S")

