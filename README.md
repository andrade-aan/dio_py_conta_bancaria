<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span>DESAFIO DE CÓDIGO - PARTE I e II</span>
</h1>

 <a href="https://web.dio.me/track/fd133067-6f2b-47c8-9763-edd87ec6b1cc"> 
     <img align="center" width="200px" src="https://hermes.dio.me/tracks/f5dba255-da18-427a-a02a-ca11a339c1cd.png">  </a>

---

# Alex Nascimento
## Estudante e Entusiasta da Ciência da Computação

### Conecte-se comigo
[![Perfil DIO](https://img.shields.io/badge/-Meu%20Perfil%20na%20DIO-400?style=for-the-badge)](https://web.dio.me/users/andrade_aan/)
[![E-mail](https://img.shields.io/badge/-Email-150?style=for-the-badge&logo=microsoft-outlook&logoColor=E94D5F)](mailto:andrade.aan@gmail.com)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=30A3DC)](https://www.linkedin.com/in/alex-andrade-nascimento/)

---
# Tecnologias Utilizadas. . .

<div style="display: inline_block">
 
  <img align="center" alt="Python" height="150" width="140" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
   <img align="center" alt="VS Code" height="150" width="140" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original-wordmark.svg">
 
## Parte I
arquivo movimentacao_bancaria.py
### Na primeira parte foi elaborado pequeno bloco de código desenvolvido em Python para simular movimentação bancária de um único cliente, utilizando um loop while = True para o Menu, sem utilização de método/funçao para realizar as operações de saque/depósito, utilizando lista para o histórico de operações na conta.<br><br>Basicamente foi utilizado if/elif/else:
 ```bash
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
```

 ### Foi utilizado somente um método para criação automática de borda.

 ```bash
def borda(texto):
    tam = len(texto)
    if tam:
        print('+','-'*tam,'+')
        print('|',texto,'|')
        print('+','-'*tam,'+')
```
---
## Parte II
- Criar funções para as operações depósito, saque e extrato, adicionando novas funcionalidades de cadastro de clientes e de conta bancária.
- Para o cadastro de clientes deverá ser usada uma lista, contendo nome, endereço, data de nascimento e CPF.
- Para o cadastro de CPF a entrada é somente de números, não podendo existir dois CPF no cadastro. Armazenar CPF como String
- As contas devem ser armazenadas em lista [agencia, numero_conta, correntista]. A conta é sequencial e começa em 1.
- Uma conta é vinculada a um único CPF, mas o CPF pode ter mais de uma conta. Agencia tem número fixo = 0001
- Poderá ser a adicionada outras funções!

O Primeiro passo foi reestruturar o código com base nas novas regras de negócio, incluindo criação de funções para atender as exigências e objetivos.

Procurei definir uma chave-primária para vincular todo o processo, no caso escolhi o número de conta, já que o CPF pode ter várias contas.
Respeitei a criação de lista para o cadastro do cliente, contudo, coloquei um dicionário com a <strong><i>key</i></strong> sendo a conta_corrente e a lista como <strong><i>value</i></strong>.

## Exemplo da Construção da função cadastrar_cliente(): 

 ```bash

def cadastrar_cliente():
   
    borda("Cadastrar novo Cliente")
   
    cpf_cliente = cadastrar_cpf()
    
    # verificação de CPF já existente no cadastro
    cpf_existe = False
    
    for key in cadastro_cliente_ag0001:
        if cadastro_cliente_ag0001[key][1] == cpf_cliente:
            cpf_exist = True
            print(f"\n\nCPF já cadastrado!!!")
            return False
   
    if cpf_cliente.isnumeric() and cpf_existe==False:
        
        print(f"\n\nCPF {cpf_cliente} cadastrado com éxito: ")
        nova_conta=criar_conta()
        log_data = instante()
    
    else:
        print("\n\nCPF inválido!")
        return False
    
    nome_cliente = str(input("\n\nDigite o nome: "))    

    endereco_cliente = str(input("\n\nEndereço - Rua/Avenida e número: "))
    
    municipio_cliente = str(input("\n\nMunicipio/UF: "))
    
    novo_cliente = [nova_conta, cpf_cliente, nome_cliente, endereco_cliente, municipio_cliente, log_data]
    
    cadastro_cliente_ag0001[nova_conta] = novo_cliente
    
    return print(f"\n\nConta n° {nova_conta} criada para {nome_cliente} já disponível para movimentação.")
    
```
## Dicionário para cadastras as operações e Biblioteca datetime

Para realizar a filtragem e segmentação das operações de cada cliente, considerando um cliente para muitas contas, utilizei outro Dicionário com a <strong><i>key</i></strong> sendo a data/hora de cada operação realizada.

De certa forma, foi criado um log para todas as operações da Agência Bancária, não sendo necessária a criação de logs individuais para cada conta de cada cliente. Para recuperar as informações, foi utilizada a <strong><i>key</i></strong> "estrangeira" conta_corrente, possibilitando a criação das funções de saldo e extrato individualizados por conta.

## Utilização da Biblioteca datetime
```bash
   
def instante(): # registrar data e hora de cada operação do sistema
    operacao_registro_hora = dt.datetime.now()
    reg_hora_operacao_formatado = operacao_registro_hora.strftime("%m/%d/%Y - %H:%M:%S")    
    return reg_hora_operacao_formatado

```
---
## Método para recuperar os dados das operações bancárias para impressão, recebendo como parâmetro o número da conta bancária
```bash
def imprimir_extrato(conta_cliente:str):
    print()
    for key in registro_operacoes:
        if conta_cliente in registro_operacoes[key][1]:
            reg = registro_operacoes[key][0]
            conta = registro_operacoes[key][1]
            tipo = registro_operacoes[key][2]
            vlr_opr = registro_operacoes[key][3]
            
            print(f"|{reg} | {conta} | {tipo.center(10)}  | {vlr_opr:.2f}")

    print("\nExtrato emitido em ",instante())


```
## Exemplo de Saída do Terminal
<img width="270" alt="image" src="https://github.com/andrade-aan/dio_py_conta_bancaria/assets/111611919/07308b99-26e1-4358-8bad-9d7cab3f832a">

---
<h3>
<a href="https://github.com/andrade-aan/dio_py_conta_bancaria_parte_3"
    target="_blank"> Parte III </a>
</h3>

### GitHub Stats
![](https://github-readme-streak-stats.herokuapp.com/?user=andrade-aan&theme=monokai&hide_border=false)<br/>
![Top Langs](https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api/top-langs/?username=andrade-aan&layout=compact&bg_color=000&border_color=30A3DC&title_color=E94D5F&text_color=FFF)

