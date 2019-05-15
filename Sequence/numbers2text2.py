#converts unicode to text
def main():
    print('Converts a sequence of Unidcode to a string of text')

    #get message
    instring = input('Please enter Unicode-encoded message')

    #loop through it
    chars = []
    for numStr in instring.split():
        codeNum = eval(numStr) #converts digits to anumber
        chars.append(chr(codeNum)) #concatentate character to message

    message = ''.join(chars)
    
    print('\nThe decoded message is: ', message)

main()
