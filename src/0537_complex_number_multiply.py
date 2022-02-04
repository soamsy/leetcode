def complexNumberMultiply(num1: str, num2: str) -> str:
    def toPythonComplex(s):
        return complex(s.replace('i', 'j').replace('+-', '-'))
    result = toPythonComplex(num1) * toPythonComplex(num2)
    return str(int(result.real)) + "+" + str(int(result.imag)) + "i"