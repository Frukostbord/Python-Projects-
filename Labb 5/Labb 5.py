import cmath
import math
import matplotlib.pyplot as plt

"""
Class for usage with polynomials
"""

class Polynomial: #Parent class Polynomial
    def __init__(self, polynomial):
        self.polynomial = polynomial
    """
    Returns highest degree of power of provided polynomial.
    e.g [0,1] = 1, [0,2,3,0] = 2
    """
    def degree(self): #Method degree
        # ignores empty lists and lists with only zeros
        if any(self.polynomial):
            degree_of_power = len(self.polynomial)

            # Reduces list length until last number != 0
            for degree in self.polynomial[::-1]:
                if degree == 0:
                    degree_of_power -= 1

                return degree_of_power - 1

        raise ValueError

    """
    Returns product from a polynomial
    e.g [0,1] with "7" provided, gives 7 (0*7**0 + 1*7**1)
    """
    def evaluate(self, x): #Method evaluate
        # Enumerates given polynomial
        polynomial = enumerate(self.polynomial)
        result = 0

        # Using our enumerated variable, we use it as degree of power
        for degree_power, number in polynomial:
            result += number * (x ** degree_power)

        return result

    """
    Returns the polynomial as a string.
    e.g [0,1,1] is x + x^2
    """
    def __str__(self):
        # Similar skeleton as lab2. First we ignore empty lists and lists with only zeros
        if any(self.polynomial):

            # Enumerate our polynomial.
            polynomial_enumerated = enumerate(self.polynomial)
            polynomial_clumped = []
            polynomial_checked = []

            # Use our enumerated variable for degree of power
            for degree, coefficient in polynomial_enumerated:
                if coefficient != 0:
                    if degree == 0:
                        polynomial_clumped.append(str(coefficient))
                    elif degree == 1:
                        polynomial_clumped.append(str(coefficient) + 'x')
                    else:
                        term = str(coefficient) + 'x^' + str(degree)
                        polynomial_clumped.append(term)

            # Removing 1´s before "x"
            for i in polynomial_clumped:
                i = i.replace("1x", "x")
                i = i.replace("-1x", "x")
                polynomial_checked.append(i)

            polynomial_string = " + ".join(polynomial_checked)
            return polynomial_string

        raise ValueError

    """
    Returns the polynomial as a graph.
    """
    def plot_poly(self, filename, x_start=-10, x_end=10, color="b"):

        x = [i for i in range(x_start, x_end+1)]
        y = []

        # We base "y" by evaluating each number in "x",
        # in our evaluate function with the polynomial given
        for coordinate in x:
            y_coordinate = self.evaluate(coordinate)
            y.append(y_coordinate)

        # Plots the graph and saves it
        plt.plot(x, y, color)
        return plt.savefig(filename + ".pdf")


"""
Subclass of "Polynomials".
"""
class QuadraticPolynomial(Polynomial):

    def __init__(self, polynomial):
        super().__init__(polynomial)

        # Checks length of Polynomial
        if len(polynomial) != 3:
            raise ValueError("Input is not a quadratic polynomial")

    """
    Quadratic formula for a second degree polynomial.
    Only works for a second degree polynomial!
    """
    def compute_roots(self):
        result = []

        # Usage of quadratic formula ("pq-formula").
        # Usage of "p" and "q" as variables to make it clearer.
        division_coefficient = [i/self.polynomial[2] for i in self.polynomial]
        q = division_coefficient[0]
        p = division_coefficient[1]


        # Discriminant (d > 0 = 2 real answers, d == 0 = 1 real answer, d < 0 = imaginary answers)
        d = p**2 - division_coefficient[2]*q*4


        # Quadratic formula
        if d >= 0:
            x_positive = (-p / 2) + math.sqrt(((p / 2) ** 2) - q)
            x_negative = (-p / 2) - math.sqrt(((p / 2) ** 2) - q)
        else:
            x_positive = (-p / 2) + cmath.sqrt(((p / 2) ** 2) - q)
            x_negative = (-p / 2) - cmath.sqrt(((p / 2) ** 2) - q)


        # Gives 1 result if they are equal, otherwise 2 results
        if d == 0:
            result.append(x_positive)
        else:
            result.append(x_negative)
            result.append(x_positive)

        return result


"""
Below are the tests for each exercise


p0 = Polynomial([0, 1])
p1 = Polynomial([0, 0, 0, 0, 1, 0])
p2 = Polynomial([0, 0, 4, 5])
p3 = Polynomial([5, 4, 3, 2, 1])

print(p0.degree())
print(p1.degree())
print(p2.degree())
print(p3.degree())


print(p0.evaluate(7))
7
print(p1.evaluate(1))
1
print(p1.evaluate(2))
16
print(p2.evaluate(0))
0
print(p2.evaluate(1))
9
print(p2.evaluate(2))
56
print(p3.evaluate(1))

print(str(p0))
#x
print(str(p1))
#x^4
print(str(p2))
#4x^2 + 5x^3
print(str(p3))
#5 + 4x + 3x^2 + 2x^3 + x^4


qp1 = QuadraticPolynomial([1, 4, 4])
qp2 = QuadraticPolynomial([1, 10, 1])
qp3 = QuadraticPolynomial([2, 4, 8])
#qp4 = QuadraticPolynomial([1, 4, 4, 4, 6])


print("The roots of",qp1,"are",qp1.compute_roots())
print("The roots of",qp2,"are",qp2.compute_roots())
print("The roots of",qp3,"are",qp3.compute_roots())

p = Polynomial([3,-1,2,1])
p.plot_poly("myplot")

"""