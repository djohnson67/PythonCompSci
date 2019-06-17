#convert Roman numerals to Decimals

def getDecimalValue(letter):
  switcher = {
   'I':1,
   'V':5,
   'X':10,
   'L':50,
   'C':100,
   'D':500,
   'M':1000
   } 
  return switcher.get(letter,-1) 

def romanNumeralsToDecimals(roman):
  decimal = 0
  currentPos = 0
  while(currentPos < len(roman)):
    val1 = roman[currentPos]
    #get value of firs character
    firstChar = getDecimalValue(val1)
    nextPos=currentPos+1
    if nextPos < len(roman):
      val2 = roman[nextPos]
      #get value of next character
      nextChar = getDecimalValue(val2)
      #compare these values
      if firstChar >= nextChar:
        #first char is greater than add it to the result
        decimal+=firstChar
        currentPos+=1
      else:
        #first char is less than next char
        decimal+=nextChar+firstChar*-1
        #skip past so there isn't a double count
        currentPos+=2
    else:
      decimal+=firstChar
      currentPos+=1

  return decimal
  


def main():
  print('This program takes a Roman numeral and converts it to a decimal')
  roms = input('Please enter the Roman Numeral to convert: ').upper()
  #roms = roms.upper();
  decimal  = romanNumeralsToDecimals(roms)
  print('The value is {0}',decimal)

if __name__ == '__main__':
  main()

