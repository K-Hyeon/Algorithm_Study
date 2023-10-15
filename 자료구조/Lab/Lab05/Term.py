class Term:
    def __init__(self, sgn, coeff, expon):
        self.sgn = sgn
        self.coeff = coeff
        self.expon = expon

    def __str__(self):
        return str(self.sgn) + str(self.coeff) + "x^" + str(self.expon) + ' '

    def getCoeff(self):
        return self.coeff

    def getExpon(self):
        return self.expon

    # sign
    def getSgn(self):
        return self.sgn
