'''print('olá, sou separador de números')
def funcao(valor,numeral):
    print(f'o {valor} desse número é {numeral}')
ah=int(input('digite um número inteiro de dígitos até o bilhão:'))
partes= {'bilhão':(ah // 100000)%1000,
         'milhão':(ah // 10000)%1000,
         'milhar':(ah // 1000)% 10 ,
         'centena':(ah // 100)% 10,
         'dezena':(ah // 10)% 10,
         'unidade':(ah // 1)%10
         }
for valor,numeral in partes.items():
  funcao(valor,numeral)'''

  