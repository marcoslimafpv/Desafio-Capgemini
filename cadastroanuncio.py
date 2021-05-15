cadastro = '====Dados do anúncio===='
print(cadastro)

visu1 = 30


investimentoDia = int(input('Valor do investimento por dia: '))

cadastro = 'Cadastro de anúncio, preencha os dados.'

nome = str(input('Digite o nome do anúncio: '))

cliente = str(input('Digite o nome do Cliente: '))

dataInicio = int(input('Data Início: '))

dataTermino = int(input('Data Término: '))

qtdDias = dataTermino - dataInicio


valorInvestido = int (investimentoDia * qtdDias)

qtdVOriginal = int (visu1 * valorInvestido)

qtdVCompart = int (qtdVOriginal / 100*12)

qtdCompart2 = int (qtdVCompart / 3 *40)


visuTotal = int (qtdCompart2 * 4 + qtdVOriginal)


valorTotalInvestido = int (dataTermino - dataInicio) * investimentoDia
print('O valor total investido é : ', valorTotalInvestido)

qtdMaxVisu = int (qtdCompart2 + qtdVCompart)
print('A quantidade de máxima de visualizações é: ', qtdMaxVisu)

qtdMaxCliques = int (qtdMaxVisu / 100) * 12
print('A quantidade máxima de cliques é: ', qtdMaxCliques)

qtdMaxCompart = int (qtdMaxCliques / 20) * 3
print('A quantidade máxima de compartilhamentos é: ', qtdMaxCompart)
