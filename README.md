# Sistema Bancário em Python

Este repositório contém um projeto desenvolvido como parte do curso da [DIO](https://www.dio.me/) em parceria com a [NTT DATA](https://www.nttdata.com/), onde foi solicitado a criação de um sistema bancário simples em Python. O projeto tem como objetivo praticar lógica de programação e manipulação de dados.

## Funcionalidades

O sistema bancário implementa as seguintes funcionalidades:

- **Depósito**: Permite ao usuário realizar depósitos em sua conta.
- **Saque**: Permite realizar saques com as seguintes restrições:
  - Limite de 3 saques diários.
  - Valor máximo por saque de R$ 500,00.
- **Extrato**: Exibe o histórico de transações (depósitos e saques) e o saldo final.
  - Os valores são formatados de acordo com o padrão brasileiro (R$ 1.365,33).
  
## Tecnologias Utilizadas

- Python 3.x
- Biblioteca `locale` para formatação de valores monetários.
- Manipulação de datas com `datetime`.

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario.git
