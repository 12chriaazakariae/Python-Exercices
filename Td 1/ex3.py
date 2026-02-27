#Password 

password = 'python123'

password_entrer = input('entrer le password : ')

while(password_entrer != password):
    print('\tMot de passe faux!!')
    password_entrer = input('entrer le password : ')

print('Exellent work!!')

