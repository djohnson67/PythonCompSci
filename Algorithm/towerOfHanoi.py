#algorithm: move n-disk tower from source to destination via resting place
# move n-1 disk tower from source to resting place
# move 1 disk tower from source to destination
# move n-1 disk tower from resting place to destination

def moveTower(n, source, dest, temp):
  if n == 1:
    print('Move disk from',source,'to',dest,'.')
  else:
    moveTower(n-1,source,temp,dest)
    moveTower(1,source,dest,temp)
    moveTower(n-1,temp,dest,source)

def hanoi(n):
  moveTower(n,'A','C','B')

def main():
  hanoi(6)

main()
