def main():
    sum = 0.0
    count = 0
    moreData = 'y'
    while moreData == 'y':
        x = eval(input('Enter a number: '))
        sum += x
        count += 1
        moreData = input('Do you have more numbers? (y or n) ')
    print('The average is', sum/count)

main()