'''print('olá, sou um identificador de ¨Santos¨')
v=str(input('me diga o nome da sua city:'))
lista= v.title()
ah= lista.split()
if lista[0] == 'Santos':
  print(f' aparentemente, a cidade {lista} começa com Santos, muuuuito original')
else:
  print(f'ah ok, a cidade {lista} não começa com Santos')'''

cid=str(input('onde nasceste?')).strip()
print(cid[:6].upper() == 'SANTOS')