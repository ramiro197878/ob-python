def suma(a, b):
    """ Calcula la suma de a y b"""
    return a + b


def resta(a, b):
    """ Calcula la resta  de a y b"""
    return a - b


def multiplica(a, b):
    """ Calcula la multiplicacion de a y b"""
    return a * b


def divide(a, b):
    """ Calcula la division de a y b"""
    if b != 0:
        return (a / b)
    else:
        return "no se puede dividir por 0"
