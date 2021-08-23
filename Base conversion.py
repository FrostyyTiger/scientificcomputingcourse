
n=92593544

r=0

solution=""

while n>0:
    r=n%15
    n= n//15
    if r > 9 :
        if r == 10:
            r = "A"
        elif r == 11:
            r = "B"
        elif r == 12:
            r = "C"
        elif r == 13:
            r = "D"
        elif r == 14:
            r = "E"
        else:
            print ("NaN")
    
    solution += str(r)  
l = len(solution)
for k in range(-1,-l-1,-1): 
    print(solution[k],end='')