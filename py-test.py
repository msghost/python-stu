n = 7
i = 2
if n>1:
    #for i in range(2,n):
    while i<n:
        print("i=",i)
        if n%i==0:
            print(n,"不是一个质数")
            break
        i+=1
    else:
        print(n,"是一个质数")
else:
    print(n,"不是一个质数")
        
