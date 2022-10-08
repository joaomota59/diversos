##maior
vet = [1,200,300,-1,1,-1111,333]

for index,i in enumerate(vet):
    if index == 0:
        maior = i
    elif maior < i:
        maior = i
print(maior)
