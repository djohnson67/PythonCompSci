
def search(x, nums):
  for i in range(len(nums)):
    if nums[i] == x:
      return i
  return -1

def main():
  res = search(2, [3,1,44,2,5])
  print('And the result is', res)

main()
  
