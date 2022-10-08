
print("Entre com as medidas dos lados do triângulo! Exemplo: 3 8 5")
A,B,C=[float(x) for x in input().split(" ")]
if A+B>C and A+C>B and B+C>A:
    if A**2==(B**2+C**2) or B**2==(A**2+C**2) or C**2==(A**2+B**2):
        print("TRIANGULO RETANGULO")
    elif A**2>(B**2+C**2) or B**2>(A**2+C**2) or C**2>(A**2+B**2):
        print("TRIANGULO OBTUSANGULO")
    elif A**2<(B**2+C**2) or B**2<(A**2+C**2) or C**2<(A**2+B**2):
        print("TRIANGULO ACUTANGULO")
    if A==B and A==C:
        print("TRIANGULO EQUILATERO")
    elif A==B and B!=C or A==C and C!=B or C==B and B!=A:
        print("TRIANGULO ISOSCELES")
else:
    print("NAO FORMA TRIANGULO")