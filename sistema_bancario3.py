import locale
from datetime import datetime

# Configura a localização para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
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

    def saque(self, *, saldo, valor, extrato, limite, numero_saques, limite_saques):
        self.resetar_limite_diario()
        
        if self.transacoes_realizadas >= limite_saques:
            print(f"\nVocê atingiu o limite de {limite_saques} transações diárias.".upper())
            return saldo, extrato
        
        if valor > self.valor_limite_saque:
            print(f"\nO valor máximo por saque é {locale.currency(self.valor_limite_saque, grouping=True)}.".upper())
            return saldo, extrato

        if valor <= saldo:
            saldo -= valor
            extrato.append((datetime.now(), 'Saque', valor, saldo))
            self.transacoes_realizadas += 1
            print(f"\nSaque de {locale.currency(valor, grouping=True)} realizado com sucesso!".upper())
        else:
            print("\nSaldo insuficiente para saque.".upper())
        
        return saldo, extrato

    def exibir_extrato(self):
        print(f"\nExtrato Bancário - Conta: {self.numero_conta} - CPF: {self.usuario['cpf']}")
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
        self.contas = []
        self.usuarios = []
        self.numero_conta_sequencial = 1  # Controla o número sequencial das contas

    def criar_usuario(self, nome, data_nasc, cpf, endereco):
        # Remove todos os caracteres não numéricos do CPF
        cpf = ''.join(filter(str.isdigit, cpf))
        if any(usuario['cpf'] == cpf for usuario in self.usuarios):
            print("Usuário com esse CPF já cadastrado.")
            return
        usuario = {'nome': nome, 'data_nasc': data_nasc, 'cpf': cpf, 'endereco': endereco}
        self.usuarios.append(usuario)
        print(f"Usuário {nome} cadastrado com sucesso!")

    def criar_conta(self, cpf):
        usuario = next((u for u in self.usuarios if u['cpf'] == cpf), None)
        if usuario:
            nova_conta = Conta(agencia="0001", numero_conta=self.numero_conta_sequencial, usuario=usuario)
            self.contas.append(nova_conta)
            print(f"Conta criada com sucesso! Número da conta: {self.numero_conta_sequencial}.")
            self.numero_conta_sequencial += 1  # Incrementa o número da conta sequencial
        else:
            print("Usuário não encontrado. Certifique-se de que o CPF esteja correto.")

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta cadastrada.")
            return
        print("\nLista de Contas:")
        for conta in self.contas:
            print(f"Agência: {conta.agencia}, Conta: {conta.numero_conta}, Nome: {conta.usuario['nome']}, CPF: {conta.usuario['cpf']}")

    def acessar_conta(self, cpf):
        return next((conta for conta in self.contas if conta.usuario['cpf'] == cpf), None)

    def deposito(self, saldo, valor, extrato):
        saldo += valor
        extrato.append((datetime.now(), 'Depósito', valor, saldo))
        print(f"\nDepósito de {locale.currency(valor, grouping=True)} realizado com sucesso!".upper())
        return saldo, extrato

# Função principal para exibir o menu e realizar operações
def main():
    banco = Banco()

    while True:
        menu = """
Escolha a opção desejada:

[1] CRIAR USUÁRIO
[2] CRIAR CONTA CORRENTE
[3] LISTAR CONTAS
[4] ACESSAR CONTA
[0] SAIR

=> """
        opcao = input(menu)

        if opcao == '1':
            nome = input("Nome do usuário: ")
            data_nasc = input("Data de nascimento (dd/mm/aaaa): ")
            cpf = input("CPF (somente números): ")
            endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            banco.criar_usuario(nome, data_nasc, cpf, endereco)

        elif opcao == '2':
            cpf = input("Digite o CPF do usuário para criar uma conta (somente números): ")
            banco.criar_conta(cpf)

        elif opcao == '3':
            banco.listar_contas()

        elif opcao == '4':
            cpf = input("Digite seu CPF para acessar sua conta (somente números): ")
            conta = banco.acessar_conta(cpf)
            if conta:
                while True:
                    menu_conta = """
Escolha a opção desejada:

[1] DEPOSITAR
[2] SAQUE
[3] SALDO E EXTRATO
[0] SAIR

=> """
                    opcao_conta = input(menu_conta)

                    if opcao_conta == '1':
                        valor = float(input("Digite o valor para depósito: R$ "))
                        conta.saldo, conta.extrato = banco.deposito(conta.saldo, valor, conta.extrato)

                    elif opcao_conta == '2':
                        valor = float(input("Digite o valor para saque: R$ "))
                        conta.saldo, conta.extrato = conta.saque(saldo=conta.saldo, valor=valor, extrato=conta.extrato, limite=conta.valor_limite_saque, numero_saques=conta.transacoes_realizadas, limite_saques=conta.limite_transacoes_diario)

                    elif opcao_conta == '3':
                        conta.exibir_extrato()

                    elif opcao_conta == '0':
                        print("Saindo da conta...")
                        break

                    else:
                        print("Opção inválida! Tente novamente.")
            else:
                print("Conta não encontrada. Verifique o CPF.")

        elif opcao == '0':
            print("Saindo... Até logo!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
