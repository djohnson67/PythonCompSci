
def search(x, nums):
  low = 0;
  high = len(nums)-1
  while low<=high:  #there is a range to search
    mid = (low + high)//2
    item = nums[mid]
    if x == item:
      return mid  
    elif x < item:
      high = mid - 1
    else:
      low = mid + 1
  return -1 # x is not there

def main():
  res = search(200, [1,2,44,200,500])
  print('And the result is', res)

main()
  