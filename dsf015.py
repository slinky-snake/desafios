print('olá, vc alugou um carro')
ah=float(input('quantos foram os km rodados? \n km:'))
ah2=int(input('e quantos foram os dias? \n dias:'))
soma= (ah* 0.15) + (ah2 * 60.0)
print(f'então, deveras pagar ao sistema {soma}R$, sendo 60R$ por dia e 0.15R$ por km rodado ')