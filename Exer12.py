lista = [""]*3
tam = len(lista)
soma = 0


for i in range(tam):
    lista[i] = int(input("Digite o número: "))

nn = int(input("Digite o numero que deseja procura: "))
for i in range(tam):
    if nn == lista[i]:
        soma+=1
print(soma)



