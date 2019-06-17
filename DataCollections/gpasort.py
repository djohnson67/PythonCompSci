
from gpa import Student, makeStudent

def readStudents(fileName):
  infile = open(fileName, 'r')
  students = []
  for line in infile:
    students.append(makeStudent(line))
  infile.close()
  return students

def writeStudents(students, filename):
  #students is a list of Student objects
  outfile = open(filename, 'w')
  for s in students:
    print('{0}\t{1}\t{2}'.format(s.getName(), s.getHours(), s.getQPoints()),file=outfile)
  outfile.close()

#def use_gpa(aStudent):
 # return aStudent.gpa()

def main():
  print('This program sorts students grad information by GPA')
  filename = input('enter the name of the data file: ')
  data = readStudents(filename)
  data.sort(key=Student.gpa)
  filename = input('Enter a name of the output file: ')
  writeStudents(data,filename)
  print('Thje data has be written to',filename)

if __name__ =='__main__':
  main()

