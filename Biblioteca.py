def piramide(n):
    for x in range(1,n+1):
        for i in range(x):
            print(x, end=" ")
        print()

def piramide2(n):
    for x in range(1,n+1):
        for i in range(1,x+1):
            print(i, end=" ")
        print()

def vogal(n):

    soma = 0
    for x in n:
        if x in "aeiouAEIOU":
            soma+=1
    print(f"O texto informado contém {soma} vogais")
n = input("Insira o texto: ")
vogal(n)



