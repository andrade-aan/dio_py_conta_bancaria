""" 
DESAFIO DE CÓDIGO

Simulação de movimentação bancária para único cliente, sem considerar diferentes clientes cadastrados.

Conta Bancária com limite de três saques diários no valor máximo de R$500.00 por operação.

Impedir saques que gerem saldo negativo.

Impedir depósitos de valor negativo.

"""
# CONSTANTES

LIMITE_SAQUE = 500.0
QTD_SAQUE_MAX = 3

# Variáveis Globais
extrato_conta = list()
contador_saques = 0
saldo_conta = 0.0

        
def borda(texto):
    tam = len(texto)
    if tam:
        print('+','-'*tam,'+')
        print('|',texto,'|')
        print('+','-'*tam,'+')

        
while True:
    
    print("\n")
    borda("Bem-vindo a sua conta corrente")
        
    print("\n1 - SACAR")
    print("2 - DEPOSITAR")
    print("3 - EXTRATO")
    print("4 - SALDO")
    print("99 - SAIR")
    
    opcao = str(input("\nDigite a opção desejada:" +
                      "\n>>> "))
    
    if opcao == '1':
       
        try:
            valor_saque = float(input("\nDigite o valor do saque:" +
                                      ">>> "))
            if valor_saque < 0:
                valor_saque *= -1
                
            if valor_saque > LIMITE_SAQUE:
                print("\nValor máximo permitido para saque é de R$500.00")
        
            elif contador_saques >= QTD_SAQUE_MAX:
                print("\nQuantidade diária de saques excedida.\n\nNão é possível realizar mais saques!!!")
            
            elif saldo_conta < valor_saque:
                print("\nSaldo insuficiente para realizar saque!!!")
            
            else:
                print(f"\nSaque no valor de R$ {valor_saque:.2f} realizado com sucesso!!!")
                extrato_conta.append("SAQUE         R$" + str(valor_saque)+"0")
                saldo_conta = saldo_conta - valor_saque
                contador_saques += 1
            
        except ValueError:
            print("\nErro ao digitar valor!!! Tente novamente...")
        
    elif opcao == '2':
        
        try:
            valor_deposito = float(input("\nDigite o valor do deposito: " +
                                         "\n>>>"))
            
            if valor_deposito <= 0:
                print("\nValor de deposito não pode ser nulo ou negativo...")
            else:
                print(f"\nDepósito no valor de R$ {valor_deposito:.2f} realizado com sucesso!!!")
                extrato_conta.append("DEPÓSITO      R$" + str(valor_deposito)+"0")
                saldo_conta = saldo_conta + valor_deposito
        
        except ValueError:
            print("\nErro ao digitar valor!!! Tente novamente...")
            
    elif opcao == '3':
        
        borda("EXTRATO - CONTA CORRENTE")
        print("\n")
        
        if not extrato_conta:
            print("\nNão há movimentações no extrato!!!")
        
        for i in range(0, len(extrato_conta)):
            print(extrato_conta[i]+"\n")
            
        
    elif opcao == '4':
        print(f"\nSeu saldo é de R${saldo_conta:.2f} !")
        
    elif opcao == '99':
        print("\n")
        borda("Obrigado por utilizar nossos serviços!!! Aplicativo Finalizado...")
        break
        
    else:
        print("Opção Inválida!!")