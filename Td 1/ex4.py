#calculatrice
repeter = 'y'

while repeter == 'y':
    num1 = int(input('entrer le premiere numero : '))
    num2 = int(input('entrer le deuxieme numero : '))

    print('1:addition | 2:soustraction | 3 :multiplication | 4 : division')
    operation = input('entrer l\'operation : ')
    match operation : 
        case '1' :
            print(f'{num1} + {num2} = {num1 + num2}')
        case '2' :
            print(f'{num1} - {num2} = {num1 - num2}')
        case '3' :
            print(f'{num1} * {num2} = {num1 * num2}')
        case '4' :
            if(num2 != 0):
                print(f'{num1} / {num2} = {num1 / num2}')
            else :
                print('division par 0 est impossible')
    repeter = input('voulez vous repeter (y/n) : ')

print('Bye Bye!!')