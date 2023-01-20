import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.compl = complex(real,imaginary) 
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
    def __mul__(self, no):
        #mul and div for complex number with special formula
        #or use complex() python default
        cMul = self.compl * no.compl
        return Complex(cMul.real,cMul.imag) #imag - value from python complex()
    def __truediv__(self, no):
        cDiv = self.compl / no.compl
        return Complex(cDiv.real,cDiv.imag)
    def mod(self):
        return Complex(abs(self.compl),0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')