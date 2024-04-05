import random

def nome():
    opcoes = ('pedra', 'papel', 'tesoura')
    while True:
        try:
            a = random.choice(opcoes)
            b = input('Pedra, papel ou tesoura? (Digite "sair" para sair): ').lower()
            if b == 'sair':
                print('Você saiu do jogo.')
                break
            elif b not in opcoes:
                print('Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.')
                continue
            elif a == b:
                print('Empate!')
            elif (a == 'pedra' and b == 'tesoura') or (a == 'papel' and b == 'pedra') or (a == 'tesoura' and b == 'papel'):
                print(f'Você escolheu {b} e eu escolhi {a}. Você perdeu!')
            else:
                print(f'Você escolheu {b} e eu escolhi {a}. Você ganhou!')
        except ValueError:
            print('Erro: Por favor, insira uma opção válida.')


nome()
