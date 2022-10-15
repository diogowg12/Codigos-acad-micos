# Lista que receberá as placas válidas
placasValidas = []

opcao = ""
print(
    "### SOFTWARE VERIFICADOR DE PLACAS DE VEÍCULOS BRASILEIROS - PADRÃO ANTIGO E NOVO ###"
)

# Verifica a opção digitada, saindo do loop apenas quando o usuário digitar a letra X.
while opcao.upper() != "X":
    contLetra = 0
    contNum = 0
    placa = input("Informe a placa do veículo:")
    # Verifica se a placa contém 7 caracteres
    if len(placa) == 7:
        # Verificar se a posição dos caracteres está correta, ou seja, letras e números no seu devido lugar.
        for i, item in enumerate(placa):
            if item.isalpha() and (i == 0 or i == 1 or i == 2 or i == 4):
                contLetra += 1
            elif item.isdigit() and (i == 3 or i == 4 or i == 5 or i == 6):
                contNum += 1

        if (contLetra == 3 and contNum == 4) or (contLetra == 4 and contNum == 3):
            # Caso a placa seja válida, insere ela na Lista de placas válidas.
            print("Placa válida!")
            placasValidas.append(placa)

        else:
            print("Placa inválida. Por favor, insira uma placa válida:")

    else:
        print("Placa inválida. Por favor, insira uma placa válida:")

    print("\n\n")
    opcao = str(input("Pressione ENTER para continuar ou 'X' para sair:"))
    print("\n\n\n\n")


# Ao final, exibe a lista de placas válidas digitas pelo usuário.
print("### PLACAS VÁLIDAS ENCONTRADAS ###")
for placasCad in placasValidas:
    print(f"Placa:{placasCad}")
