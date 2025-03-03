"""
    n=6
    1
    7 2
    12 8 3
    16 13 9 4
    19 17 14 10 5
    21 20 18 15 11 6
"""
n=6
for i in range(1,n+1):
    start = sum(range(n,n-i,-1))+1
    for j in range(start,start-i,-1):
        print(j,end=" ")
    print("")





