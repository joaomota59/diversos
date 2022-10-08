##maior
vet = [1,200,300,-1,1,-1111,333]

def maior(vetor):
    maior = None
    for index,i in enumerate(vetor):
        if index == 0:
            maior = i
        elif maior < i:
            maior = i
    return maior


print(maior(vet))
