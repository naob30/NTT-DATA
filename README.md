# Sistema Bancário em Python

Este repositório contém um projeto desenvolvido como parte do curso da [DIO](https://www.dio.me/) em parceria com a [NTT DATA](https://www.nttdata.com/), onde foi solicitado a criação de um sistema bancário simples em Python. O projeto tem como objetivo praticar lógica de programação e manipulação de dados.

## Funcionalidades

O sistema bancário implementa as seguintes funcionalidades:

**Gerenciamento de Usuários:**
Cadastro de novos usuários com informações como nome, data de nascimento, CPF e endereço.
Validação para garantir que não haja duplicação de CPF.

**Gerenciamento de Contas Correntes:**
Criação de contas correntes vinculadas a um usuário existente.
A conta possui um número sequencial e uma agência fixa.

**Operações Bancárias:**
Depósito: Permite adicionar um valor ao saldo da conta. O depósito é registrado no extrato.
Saque: Permite retirar um valor do saldo da conta, respeitando um limite de saques diários e um valor máximo por saque. O saque também é registrado no extrato.
Extrato: Exibe todas as transações realizadas em uma conta, incluindo depósitos e saques, com a data e o saldo após cada transação.

**Listagem de Contas:**
Exibe uma lista de todas as contas cadastradas no sistema, mostrando informações como agência, número da conta e dados do usuário.
  
## Tecnologias Utilizadas

- Python 3.x
- Biblioteca `locale` para formatação de valores monetários.
- Manipulação de datas com `datetime`.

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario.git
