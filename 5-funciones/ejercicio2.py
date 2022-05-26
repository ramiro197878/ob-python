# Escribe una función que pueda decirte si un número (número entero)
# es primo o no.


def es_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return f'El número %s no es primo' %(numero)
    return f'El número %s es primo' %(numero)

print(es_primo(5))
print(es_primo(11))
print(es_primo(4))
print(es_primo(33))
print(es_primo(22))
