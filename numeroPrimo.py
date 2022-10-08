x=int(input("Entre com um número: "))
soma=0
for j in range(1,x):
    if x%j==0:
        soma+=1
if soma==1:
    print(x,"eh primo")
else:
    print(x,"nao eh primo")
