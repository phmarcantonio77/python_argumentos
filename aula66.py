
"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o valor (A ordem importa )
"""

def soma(x, y):
    print(f'{x=} {y=}', '|', 'x+y =', x + y)


# -------------------------------
# Argumentos não nomeados (posicionais)
# -------------------------------
print("Argumentos posicionais (a ordem importa):")

soma(1, 3)  # x=1, y=3
soma(3, 1)  # x=3, y=1

print()
# -------------------------------
# Argumentos nomeados
# -------------------------------
print("Argumentos nomeados (a ordem não importa):")

soma(x=2, y=4)
soma(y=4, x=2)