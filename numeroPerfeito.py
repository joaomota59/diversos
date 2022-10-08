print("Entre com um número")

x=int(input())
soma=0
for j in range(1,x):
    if x%j==0:
        soma+=j
if soma==x:
    print(x,"eh perfeito")
else:
    print(x,"nao eh perfeito")

