print("Entre com os valores de a b c da equação ax²+bx+c Exemplo: 2 6 4")

a,b,c=[float(x) for x in input().split(" ")]
delta=(b**2)-(4*a*c)
import math
if delta<0 or a==0:
    print("Impossivel calcular")
else:
    raiz=math.sqrt(delta)
    x1=(-b+raiz)/(2*a)
    x2=(-b-raiz)/(2*a)
    print("R1 = %.5f"%x1)
    print("R2 = %.5f"%x2)