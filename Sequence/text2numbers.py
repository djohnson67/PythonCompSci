#convert text message to numbers
def main():
    print('Converts a text message into a sequence')
    print('of numbers representing the Unicode encoding of the message. \n')
    #get message to encode
    message = input('Please enter message to encode: ')
    print('Here are the Unicode codes: ')

    #loop through and print out message
    for ch in message:
        print(ord(ch), end=' ')
    
    print()

main()
