import locale
from datetime import datetime

# Configura a localização para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_realizados = 0  # Número de saques feitos no dia
        self.limite_saques_diario = 3  # Limite de saques
        self.valor_limite_saque = 500  # Valor máximo por saque

    def deposito(self, valor):
        self.saldo += valor
        self.extrato.append((datetime.now(), 'Depósito', valor, self.saldo))
        print(f"\nDepósito de {locale.currency(valor, grouping=True)} realizado com sucesso!".upper())

    def saque(self, valor):
        if self.saques_realizados >= self.limite_saques_diario:
            print(f"\nVocê atingiu o limite de {self.limite_saques_diario} saques diários.".upper())
            return

        if valor > self.valor_limite_saque:
            print(f"\nO valor máximo por saque é {locale.currency(self.valor_limite_saque, grouping=True)}.".upper())
            return

        if valor <= self.saldo:
            self.saldo -= valor
            self.saques_realizados += 1
            self.extrato.append((datetime.now(), 'Saque', valor, self.saldo))
            print(f"\nSaque de {locale.currency(valor, grouping=True)} realizado com sucesso!".upper())
        else:
            print("\nSaldo insuficiente para saque.".upper())

    def exibir_extrato(self):
        print("\nExtrato Bancário")
        print("-" * 68)
        print(f"{'Data/Hora':<20} | {'Tipo':<10} | {'Valor':<15} | {'SALDO':<14}")
        print("-" * 68)
        for transacao in self.extrato:
            data, tipo, valor, saldo = transacao
            print(f"{data.strftime('%d/%m/%Y %H:%M'):<20} | {tipo:<10} | {locale.currency(valor, grouping=True):<15} | {locale.currency(saldo, grouping=True):<15}")
        print("-" * 68)
        print(f"Saldo Final: {locale.currency(self.saldo, grouping=True)}\n".upper())


# Função principal para exibir o menu e realizar operações
def main():
    banco = Banco()
    
    while True:
        menu = """
Escolha a opção desejada:

[1] DEPOSITAR
[2] SAQUE
[3] SALDO E EXTRATO
[0] SAIR

=> """
        opcao = input(menu)

        if opcao == '1':
            valor = float(input("Digite o valor para depósito: R$ "))
            banco.deposito(valor)
        
        elif opcao == '2':
            valor = float(input("Digite o valor para saque: R$ "))
            banco.saque(valor)
        
        elif opcao == '3':
            banco.exibir_extrato()

        elif opcao == '0':
            print("Saindo... Até logo!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
