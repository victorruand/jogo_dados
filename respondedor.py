import time, random 

respostas = [
    'não', 'não' 'sei', 'não tá', 'sim' , 'sim sei','tudo', 'triste', 'feliz', 'bem', 'mal', 'ruim',
    'péssimo', 'fé', 'sim vai lá', 'não siow', 'sim siow',  'claro!', 'acho que sim', 'acho que não', 'isso não faz muito sentido',
    'ah para', 'claro que sim',
    ]
fala = ['fala aí: ', 'vai: ', 'diz aí:', 'vaaai: ', 'vai siow: ', 'manda a braba: ' ]
continuar = True
while continuar:
    #esta var é para radomizar a pergunta
    randomm  = fala[random.randint(0,5,)]
    pergunta = input('Quer conversar? [SIM ou NÃO]:  ').upper()
    if pergunta == 'SIM':
        print('pensando ...!')
        time.sleep(2)
        print('tá bom,eu também quero!')
        question = input(randomm)
        time.sleep(random.randint(1,2))
        print('umm..')
        print(respostas[random.randint(1,len(respostas))])
        time.sleep(2)
        time.sleep(1)
    elif pergunta == 'NÃO':
        time.sleep(2)
        print('Ah porra')
        continuar = False
    else:
        print('Digita pelo menos certo sio ')
    

