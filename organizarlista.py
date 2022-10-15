# organizarlista

tabela = []
tamanho = int(input("Digite o tamanho da lista: "))
for j in range(tamanho):
    valor = float(input("Digite um novo valor para a lista: "))
    tabela.append(valor)


print("Lista informada: {tabela}")


mudar = True
while mudar:
    mudar = False
    for i in range(len(tabela) - 1):
        if tabela[i] > tabela[i + 1]:
            aux = tabela[i]
            tabela[i] = tabela[i + 1]
            tabela[i + 1] = aux
            mudar = True


print(f"Lista organizada: {tabela}")
