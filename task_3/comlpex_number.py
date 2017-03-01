class ComplexNumber:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        """

        :type other: ComplexNumber
        """
        return ComplexNumber(self.real + other.real,
                             self.imaginary + other.imaginary)

    def __sub__(self, other):
        """

        :type other: ComplexNumber
        """
        return ComplexNumber(self.real - other.real,
                             self.imaginary - other.imaginary)

    def __mul__(self, other):
        """

        :type other: ComplexNumber
        """
        return ComplexNumber(self.real * other.real -
                             self.imaginary * other.imaginary,
                             self.real * other.imaginary +
                             self.imaginary * other.real)

    def __truediv__(self, other):
        """

        :type other: ComplexNumber
        """
        new_complex = self * ComplexNumber(real=other.real,
                                           imaginary=-other.imaginary)
        norm = (other.real ** 2 + other.imaginary ** 2)
        new_complex.real /= norm
        new_complex.imaginary /= norm
        return new_complex

    def __str__(self):
        if self.real != 0.0 and self.imaginary != 0.0:
            return "{0:.2f} {1} {2:.2f}i".format(self.real,
                                                 "-"
                                                 if self.imaginary < 0
                                                 else "+",
                                                 abs(self.imaginary))
        elif self.real == 0.0 and self.imaginary != 0.0:
            return "{0:.2f}i".format(self.imaginary)
        else:
            return "{0:.2f}".format(self.real)


with open('input.txt', 'r') as in_file:
    for line in in_file:
        print(eval(line))
