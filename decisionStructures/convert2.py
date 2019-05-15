def main():
    celsius = int(input('What is the Celsius temperature? '))
    fahrenheit = 9/5 * celsius + 32

    print('the temparture is', fahrenheit,'degrees Fahrenheit.')
    #print warnings
    if(fahrenheit > 90):
        print('It\'s a hot one out there. Be careful')
    if(fahrenheit<30):
        print('Brrrrr. Be sure to dress warm.')

main()

