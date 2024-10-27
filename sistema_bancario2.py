import locale
from datetime import datetime

# Configura a localização para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Conta:
    def __init__(self, cpf):
        self.cpf = cpf
        self.saldo = 0
        self.extrato = []
        self.transacoes_realizadas = 0
        self.limite_transacoes_diario = 10
        self.valor_limite_saque = 500
        self.ultima_transacao_data = datetime.now().date()

    def resetar_limite_diario(self):
        hoje = datetime.now().date()
        if hoje != self.ultima_transacao_data:
            self.transacoes_realizadas = 0
            self.ultima_transacao_data = hoje

    def deposito(self, valor):
        self.resetar_limite_diario()
        
        if self.transacoes_realizadas >= self.limite_transacoes_diario:
            print(f"\nVocê atingiu o limite de {self.limite_transacoes_diario} transações diárias.".upper())
            return
        
        self.saldo += valor
        self.extrato.append((datetime.now(), 'Depósito', valor, self.saldo))
        self.transacoes_realizadas += 1
        print(f"\nDepósito de {locale.currency(valor, grouping=True)} realizado com sucesso!".upper())

    def saque(self, valor):
        self.resetar_limite_diario()
        
        if self.transacoes_realizadas >= self.limite_transacoes_diario:
            print(f"\nVocê atingiu o limite de {self.limite_transacoes_diario} transações diárias.".upper())
            return

        if valor > self.valor_limite_saque:
            print(f"\nO valor máximo por saque é {locale.currency(self.valor_limite_saque, grouping=True)}.".upper())
            return

        if valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append((datetime.now(), 'Saque', valor, self.saldo))
            self.transacoes_realizadas += 1
            print(f"\nSaque de {locale.currency(valor, grouping=True)} realizado com sucesso!".upper())
        else:
            print("\nSaldo insuficiente para saque.".upper())

    def exibir_extrato(self):
        print(f"\nExtrato Bancário - CPF: {self.cpf}")
        print("-" * 68)
        print(f"{'Data/Hora':<20} | {'Tipo':<10} | {'Valor':<15} | {'SALDO':<14}")
        print("-" * 68)
        for transacao in self.extrato:
            data, tipo, valor, saldo = transacao
            print(f"{data.strftime('%d/%m/%Y %H:%M'):<20} | {tipo:<10} | {locale.currency(valor, grouping=True):<15} | {locale.currency(saldo, grouping=True):<15}")
        print("-" * 68)
        print(f"Saldo Final: {locale.currency(self.saldo, grouping=True)}\n".upper())


class Banco:
    def __init__(self):
        self.contas = {}

    def acessar_conta(self, cpf):
        if cpf not in self.contas:
            print("Conta não encontrada. Criando uma nova conta...")
            self.contas[cpf] = Conta(cpf)
        return self.contas[cpf]

    def deposito(self, conta, valor):
        conta.deposito(valor)

    def saque(self, conta, valor):
        conta.saque(valor)

    def exibir_extrato(self, conta):
        conta.exibir_extrato()


# Função principal para exibir o menu e realizar operações
def main():
    banco = Banco()
    cpf = input("Digite seu CPF para acessar sua conta (somente números): ")
    conta = banco.acessar_conta(cpf)
    
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
            banco.deposito(conta, valor)
        
        elif opcao == '2':
            valor = float(input("Digite o valor para saque: R$ "))
            banco.saque(conta, valor)
        
        elif opcao == '3':
            banco.exibir_extrato(conta)

        elif opcao == '0':
            print("Saindo... Até logo!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

        # Pergunta ao usuário se deseja trocar o CPF após sair
        if opcao == '0':
            novo_acesso = input("Deseja acessar uma conta com um novo CPF? (s/n): ").lower()
            if novo_acesso == 's':
                cpf = input("Digite seu novo CPF para acessar a conta (somente números): ")
                conta = banco.acessar_conta(cpf)

# Executa o programa
if __name__ == "__main__":
    main()

