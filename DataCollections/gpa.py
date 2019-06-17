#gpa.py
#find student with highest gpa

class Student:
  def __init__(self,name, hours,qpoints):
    self.__name = name
    self.__hours = float(hours)
    self.__qpoints = float(qpoints)

  def getName(self):
    return self.__name

  def getHours(self):
    return self.__hours

  def getQPoints(self):
    return self.__qpoints

  def gpa(self):
    return self.__qpoints/self.__hours

    

def makeStudent(infoStr):
  #tab separated line
  name, hours, qpoints = infoStr.split('\t')
  return Student(name, hours, qpoints)

def main():
  #open file for input
  fileName = input('Enter the name of the input file: ')
  infile = open(fileName, 'r')

  #set best to the first recoerd
  best = makeStudent(infile.readline())

  #process the rest of the file
  for line in infile:
    #turn each line into a student record
    s = makeStudent(line)
    #test each line and remember the bvest
    if s.gpa() > best.gpa():
      best = s

  infile.close()

  #print the best
  print('The best student is: ', best.getName())
  print('Hours: ', best.getHours())
  print('GPA', best.gpa())

if __name__ == '__main__':
  main()
  