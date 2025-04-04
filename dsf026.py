v=str(input('diga uma frase:')).lower()
print(f'a letra A aparece {v.count('a')}, vezes\n o primeiro A aparece na posição {v.find('a')+1}, \n e  a ultima na {v.rfind('a')+1} posição')
