for i in range(int(input())):
    a,b=[str(i) for i in input().split()]
    k=""
    for i in range(max([len(a),len(b)])):
        try:
            k+=a[i]+b[i]
        except:
            try:
                k+=a[i]
            except:
                k+=b[i]
    print(k)
