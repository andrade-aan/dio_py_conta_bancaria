<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span>DESAFIO DE CÓDIGO</span>
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
 
 ### Pequeno bloco de código desenvolvido em Python para simular movimentação bancária de um único cliente, utilizando um loop while = True para o Menu, sem utilização de método/funçao para realizar as operações de saque/depósito, utilizando lista para o histórico de operações na conta.<br><br>Basicamente foi utilizado if/elif/else:
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
 
### GitHub Stats
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=andrade-aan&theme=transparent&bg_color=000&border_color=30A3DC&show_icons=true&icon_color=30A3DC&title_color=E94D5F&text_color=FFF)
![Top Langs](https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api/top-langs/?username=andrade-aan&layout=compact&bg_color=000&border_color=30A3DC&title_color=E94D5F&text_color=FFF)

