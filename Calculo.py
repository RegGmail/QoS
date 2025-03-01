class Calculo (object):
    def somar (self, x, y):
        if type(x) == int and type(y) == int:
            return (x + y)
        else:
            raise TypeError ("Tipo Inválido: {} and {}".format (type(x), type(y)))
    
if __name__ == '__main__':
    calc = Calculo()
    resultado = calc.somar (3, 5)
    print (resultado)

    resultado = calc.somar ("Ola ", 3)
    print (resultado)

