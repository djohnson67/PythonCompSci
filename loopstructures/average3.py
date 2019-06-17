def main():
    sum = 0.0
    count = 0
    x = eval(input('Enter a number (Negative to quit): '))
    while x >= 0:
        sum += x
        count += 1
        x = eval(input('Enter a number (Negative to quit): '))
    print('The average is', sum/count)

main()