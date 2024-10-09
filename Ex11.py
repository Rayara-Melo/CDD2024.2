#FAÇA UMA FUNÇÃO QUE CONTE QUANTAS VOGAIS TEM UM TEXTO.
# #TEXTO: O rato roeu a roupa do Rei de Roma

n = input("Insira o texto: ")
soma = 0
for x in n:
        if x in "aeiouAEIOU":
            soma += 1
print(f"O texto informado contém {soma} vogais")
