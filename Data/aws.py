import re

def getFile(fileName, attrib):
  return open(fileName, attrib)

def main():
  filterFile =getFile('Data/filters.txt','rt')
  filterString = []

  #ingest the filters
  for line in filterFile:
    filterString.append(line.strip())

  filterFile.close()
  combine =  "(" + ")|(".join(filterString) + ")"
  awsFile = getFile('Data/aws.txt','rt')
  awsOutfile = getFile('Data/awsOutfile','wt')
 
  awsInfileCount = 0
  awsOutfilecount = 0
  
  try:
    for line in awsFile:
      awsInfileCount +=1
      if re.search(combine, line):
        awsOutfilecount  +=1
        awsOutfile.write(line)
  
  except:
    pass
  
  awsFile.close()
  awsOutfile.close()

  print("Total Lines Read",awsInfileCount)
  print("Total Lines Wrote",awsOutfilecount)

if __name__ == '__main__':
  main()
  