'''import math
print('olá, eu meço para vc um triânguo retângulo\n')
co=float(input('me dê o cateto oposto:'))
ca=float(input('me dê p adjacente:'))
hip= (ca**2 + co**2)
raiz=math.sqrt(hip)
print(f'ok, o calculo gera uma hipotenusa de{raiz:.2f} ')'''

import math
print('olá, eu meço para vc um triângulo retângulo\n')
co=float(input('me dê o cateto oposto:'))
ca=float(input('me dê p adjacente:'))
hip= math.hypot(co,ca)
print(f'ok, o calculo gera uma hipotenusa de{hip:.2f} ')