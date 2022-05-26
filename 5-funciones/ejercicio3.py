# Escribe una función que pueda decirte si un año (número entero) es bisiesto
# o no.


def es_bisiesto(numero):
    if numero % 4 == 0 and numero % 100 != 0:
        return f'El año %s es bisiesto' %(numero)
    elif numero % 100 == 0 and numero % 400 == 0:
        return f'El año %s es bisiesto' %(numero)
    else:
        return f'El año %s no es bisiesto' %(numero)


print(es_bisiesto(1904))
print(es_bisiesto(2000))
print(es_bisiesto(1998))
print(es_bisiesto(1604))
print(es_bisiesto(2095))
print(es_bisiesto(2044))
print(es_bisiesto(2012))
print(es_bisiesto(2100))
print(es_bisiesto(2200))
