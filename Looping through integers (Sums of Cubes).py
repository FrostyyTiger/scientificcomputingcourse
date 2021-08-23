for d in range (1,1001):
    for c in range(1,d):
        for b in range(1,c):
            for a in range(1,b+1):
                if a**3 + b**3 + c**3 == d**3:
                    print(a,b,c,d)