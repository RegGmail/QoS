# Calculate
class Calculate (object):
    def add (self, x, y):
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError ("Invalid type: {} and {}".format (str(type(x)), str(type(y))))

if __name__ == '__main__': #Pragma: no cover
    calc = Calculate() #Pragma: no cover
    result = calc.add("Hello","World") #Pragma: no cover
    print (result) #Pragma: no cover

