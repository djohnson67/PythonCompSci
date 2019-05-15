import math
def main():
  print('This program finds tghe real solutions to a quadratic\n')
  
  try:
    a,b,c = eval(input('Please enter the coefficients (a,b,c): '))
    discrim = b*b - 4 * a * c
    discRoot = math.sqrt(discrim)
    root1 = (-b + discRoot)/ (2*a)
    root2 = (-b - discRoot)/ (2*a)
    print('\nThe solutions are: ',root1,root2)
  except ValueError as escObj:
    if str(escObj) == 'math domain error':
      print('The equation has no roots!')
    else:
      print('You didn\'t give me the right number of cofficients')
  except NameError:
    print('\nYou didn\'t enter three numbers.')
  except TypeError:
    print('\nYour inputs were not all numbers. ')
  except SyntaxError:
    print('\nYour input was not in the correct form. Missing coma? ')
  except:
    print('\nSomething went wrong. ')
       

main()
