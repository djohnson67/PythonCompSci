import re
import csv
import sys

def getFile(fileName, attrib):
  return open(fileName, attrib)

def main():
  filterFile =getFile('Data/filters.txt','rt')
  filterString = []

  #ingest the filters
  for line in filterFile:
    filterString.append(line.strip())

  filterFile.close()
  #create a list of regular expressions from filters array
  combine =  "(" + ")|(".join(filterString) + ")"
  awsInfileCount = 0
  awsOutfilecount = 0
  
  try:
    with open(input('Please enter the name of the input file: '),'rt') as awsInFile:
      awsInFileReader = csv.reader(awsInFile)
      awsOutfile = getFile(input("Please enter the name of the output file: "),'wt')
      for row in awsInFileReader:
        awsInfileCount +=1 
        if re.search(combine, row[13]):
          awsOutfilecount +=1
          awsOutfile.write(line)
  except FileNotFoundError:
    print("File not found")
    exit()
  except:
    pass
  
  awsInFile.close()
  awsOutfile.close()

  print("Total Lines Read",awsInfileCount)
  print("Total Lines Wrote",awsOutfilecount)

if __name__ == '__main__':
  main()
  