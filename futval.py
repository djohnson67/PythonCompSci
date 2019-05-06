#future value of investment in 10 years
def main():
    print('Calculates future value of a 10 year investment')

    principal = eval(input('Enter initial value of investment: '))
    apr = eval(input('Enter the annual interest rate: '))

    for i in range(10):
        principal = principal * (1+apr)
    
    print('The value in 10 years is:', principal)

main()
