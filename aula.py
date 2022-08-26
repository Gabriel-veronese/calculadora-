'''print('Digite a quantidade da parcela:')      ###CONTADOR DE PARCELAS###
qtd = int(input())
print(qtd)
soma = 0

while qtd <= 2:
    print('Número de parcelas ínvalida')
    print('Digite um número de parcelas valido:')
    qtd = int(input())

for contx in range(qtd):
    print('Digite o valor da parcela:')
    vlr = int(input())
    soma=soma+vlr
    print(soma)
'''
n1 = float(input('Digite o primeiro número:'))                     ### Calculadora Simples ###
n2 = float(input('Digite o segundo número:'))
opc = int(input('Escolha uma opcao: \n[1]Adição \n[2]Subtração \n[3]Multiplicação \n[4]Divisão \n[5]Sair \n'))

if opc == 1:
    print('Soma:', n1+n2)
if opc == 2:
    print('Subtração:', n1-n2)
if opc == 3:
    print('Multiplicação:', n1*n2)
if opc == 4: 
    print('Divisão:', n1/n2)
if opc == 5: 
    print('Saindo da Calculadora...')
    exit()
