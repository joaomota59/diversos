vet=[0,1]
for i in range(int(input())):
    N=int(input())
    if N==0:
        print("Fib(0) = 0")
    elif N==1:
        print("Fib(1) = 1")
    else: 
        for i in range(60):
            if len(vet)>60:
                break
            vet.append(vet[i]+vet[i+1])
        print("Fib(%d) = %d"%(N,vet[N]))
