for i in range (int(input())):
    A,B=[int(x) for x in input().split(" ")]
    A=str(A)
    B=str(B)
    x=len(A) - len(B)
    A=A[x:]
    if B==A:
        print("encaixa")
    else:
        print("nao encaixa")
