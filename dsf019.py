import random

um=input('me dê o nome de um aluno:')
dois=input('um segundo aluno:')
tres=input('um terceiro aluno:')
quatro=input('um quarto aluno:')
soma= random.choice([um , dois , tres , quatro])
print(f'o aluno selecionado será:{soma}')