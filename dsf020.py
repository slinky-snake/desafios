from random import shuffle
print('bom professor, agora me diga o nome dos seus 4 alunos e direi a ordem de aprentação deles:')
a=str(input('aluno 1:'))
b=str(input('aluno 2:'))
c=str(input('aluno 3:'))
d=str(input('aluno 4:'))
lista = [a,b,c,d]
shuffle(lista)
print(f'ok então, a ordem será {lista}')