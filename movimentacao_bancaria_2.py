"""
Criar funções para as operações depósito, saque e extrato, 
adicionando novas funcionalidades de cadastro de clientes e de conta bancária.
Para o cadastro de clientes deverá ser usada uma lista, contendo nome, endereço, data de nascimento e CPF.
Para o cadastro de CPF a entrada é somente de números, não podendo existir dois CPF no cadastro.
Armazenar CPF como String
As contas devem ser armazenadas em lista [agencia, numero_conta, correntista].
A conta é sequencial e começa em 1.
Uma conta é vinculada a um único CPF, mas o CPF pode ter mais de uma conta.
Agencia tem número fixo = 0001
Poderá ser a adicionada outras funções!

"""
import datetime as dt

# CONSTANTES

LIMITE_SAQUE = 500.0
QTD_SAQUE_MAX = 3

# Variáveis Globais
extrato_conta = list()
contador_saques = 0
saldo_conta = 0.0

def instante():
    operacao_registro_hora = dt.datetime.now()
    reg_hora_operacao_formatado = operacao_registro_hora.strftime("%m/%d/%Y - %H:%M:%S")    
    return reg_hora_operacao_formatado

def sacar():
    print()

def depositar():
    print()

def imprimir_extrato():
    print()

def cadastrar_conta():
    print()
    
def cadastrar_cliente():
    print()

        
def borda(texto):
    tam = len(texto)
    if tam:
        print('+','-'*tam,'+')
        print('|',texto,'|')
        print('+','-'*tam,'+')


def menu_principal():
    print("\n1 - SACAR")
    print("2 - DEPOSITAR")
    print("3 - EXTRATO")
    print("4 - SALDO")
    print("5 - GERENCIA")
    print("99 - SAIR")        

def menu_gerencia():
    borda("Menu de Gerência Agência 0001 - Bem-vindo!")
    print(instante())
    print("\n1 - CADASTRAR CONTA")
    print("2 - CADASTRAR CLIENTE")
    print("3 - LISTAR CLIENTES")
    print("4 - SAIR")

while True:
    
    print("\n")
    borda("Bem-vindo a sua conta corrente")
    
    print(instante())        
    menu_principal()
    
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
        
    elif opcao == '5':
        menu_gerencia()    
        
    elif opcao == '99':
        print("\n")
        borda("Obrigado por utilizar nossos serviços!!! Aplicativo Finalizado...")
        break
        
    else:
        print("Opção Inválida!!")