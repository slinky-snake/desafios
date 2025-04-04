from itertools import count

print('olá, me diga seu nome.')
ah=input('escreva aqui:')

print(f'esse é seu nome capitalizado:[ {ah.title()} ]')# pode-se por .strip para remover espaços
print(f'esse é seu nome em minúsculas:{ah.lower()}')
print(f'esse é seu nome em minúsculas:{ah.upper()}')
print(f'seu nome tem {len(ah.replace(' ',''))} letras')#ou tbm -ah.count()
nova=ah.split()
print(f'e seu primeiro nome é {nova[0]} e tem {len(nova[0])} letras')# ou ah.find('  ')
