#Contar quantas pessoas estão em ensinos

cont18 = conth = contm20 = 0
while True:
    escola = str(input(
        'Digite a escolaridade do aluno sendo que 1 = ensino fundamental 2 = ensino médio e 3 = ensino superior[1/2/3]:')).upper().strip()[0]
    if escola != '1' and escola != '2' and escola != '3':
        print('Escolariade invalida. Tende novamente.')
    else:
        if escola == '1':
            cont18 += 1
        if escola == '2':
            conth += 1
        if escola == '3':
            contm20 += 1
    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print(
    f'Total de pessoas com esnino fundamental é: {cont18}\nCom ensino médio é: {conth}\nE com ensino superior é:{contm20}')
