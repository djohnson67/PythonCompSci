import re
import csv

def getFile(fileName, attrib):
  return open(fileName, attrib)

def main():
  csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_NONE)
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
    #with open(input('Please enter the name of the input file: '),'r') as awsInFile:
    with open('Data/aws.csv','r') as awsInFile:
      awsInFileReader = csv.reader(awsInFile) 
      header = next(awsInFileReader) #skip the first row - it's a header row
      #with open(input("Please enter the name of the output file: "),'w', newline='') as fout:
      with open('Data/awsOutfile.csv','w', newline='') as fout:
        awsOutfile = csv.writer(fout, delimiter=',')
        awsOutfile.writerow(header)
        detailsColumn = 13
        for row in awsInFileReader:
          awsInfileCount += 1 
          if re.search(combine, row[detailsColumn]):
            awsOutfilecount += 1
            awsOutfile.writerow(row)
  except FileNotFoundError:
    print("File not found")
    exit()
  except:
    pass
  
  awsInFile.close()
  fout.close()

  print("Total Lines Read",awsInfileCount)
  print("Total Lines Wrote",awsOutfilecount)

if __name__ == '__main__':
  main()
  