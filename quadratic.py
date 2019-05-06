#real roots of quadratic expressions
import math #math library

def main():
    print('Finds the real solution to a quadratic')
    print()

    a,b,c = eval(input('Please enter the coefficients (a, b, c,): '))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print('The solutions are: ', root1, root2)

main()