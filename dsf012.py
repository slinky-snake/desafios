pq=float(input('qual o preço do produto?R$'))
desc=int(input('e o desconto?%'))
pc= pq * desc/10
print(f'o produto de {pq}reais, agora custa {pc:.3f} R$ com {desc}% de desconto!\n' )

prod=input('quer saber o desconto de um produto?')
if prod =="sim":
    valor1 = float(input('qual o valor anterior?R$'))
elif prod != 'sim':
    print('ok, até depois')

novo = float(input('qual o valor atual?'))
diferença = valor1 - novo
desconto=(diferença/valor1) *10
ah=int(desconto)
print(f'ok, o produto de {valor1}R$, que agora é {novo}R$, teve {ah}% de desconto.')