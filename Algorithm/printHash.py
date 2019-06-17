def main():

  
  maxi = 4
  for j in range(maxi):
    for i in range(maxi - j):
       print('#', end='')
    print ('')    
  
  maxi = 8
  for j in range(maxi):
    print(4 - abs(4-j))
   

main()