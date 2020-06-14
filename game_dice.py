import time, random


class game_dice:
    def __init__(self):
        self.name = ""
        self.answer = ""
    
    def jogo_em_si(self):
        continuar = True
        self.name = input('Digite seu nome: ')
        
        while continuar:
            self.answer = input(self.name + ', você gostaria de jogar o dado? ').upper()
            if self.answer == 'SIM':
                self.resultado = random.randint(1, 6)
                print('O resultado é: ', self.resultado)

                self.answer = input('Você gostaria de jogar navamente?').upper()
                if self.answer == 'NÃO':
                    continuar = False
                    print('Tá bom, ' + self.name + ' foi muito bom jogar com você!')
                elif self.answer == 'SIM':
                    print('Que legaal!')
                    time.sleep(2)

            elif self.answer == 'NÃO':
                print('Ahh que pena..')
                continuar = False

            else:
                print('FORMATO INVÁLIDO:  Digite SIM ou NÃO!')
                continuar = True

play1 = game_dice()
play1.jogo_em_si()
