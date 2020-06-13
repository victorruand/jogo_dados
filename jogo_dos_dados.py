import time, random
from time import sleep


continuar = True
name = input('Digite seu nome: ')

while continuar:    
    answer = input(name +', você gostaria de jogar o dado? ').upper()
    if answer == 'SIM':
        resultado = random.randint(1,6)
        print('O resultado é: ', resultado)
        
        answer = input('Você gostaria de jogar navamente?').upper()
        if answer == 'NÃO':
            continuar = False
            print('Tá bom, '+ name +' foi muito bom jogar com você!')
        elif answer == 'SIM':
            print('Que legaal!')
            time.sleep(2)
            
    elif answer == 'NÃO':   
        print('Ahh que pena..')
        continuar = False
   
    else: 
        print ('FORMATO INVÁLIDO:  Digite SIM ou NÃO!')
        continuar = True

#FAZER TUDO ISSO COM CLASSES E MÉTODOS!