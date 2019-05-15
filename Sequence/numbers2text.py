#converts unicode to text
def main():
    print('Converts a sequence of Unidcode to a string of text')

    #get message
    instring = input('Please enter Unicode-encoded message')

    #loop through it
    message = ''
    for numStr in instring.split():
        codeNum = eval(numStr) #converts digits to anumber
        message += chr(codeNum) #concatentate character to message

    print('\nThe decoded message is: ', message)

main()
