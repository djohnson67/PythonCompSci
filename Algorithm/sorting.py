def selSort(nums):
  #sor nums in ascending order
  n = len(nums)

  #for each position in the list (except the last)
  for bottom in range( n - 1):
    #find smallest item in nums[bottom].. nums[n-1]
    mp = bottom   #initally the smallest

    for i in range(bottom+1, n): #look at each postion
      if nums[i] < nums[mp] :     #this one is smaller
        mp = i                    #remember its indexz
    
    nums[bottom], nums[mp] = nums[mp],nums[bottom]

def merge(lst1, lst2, lst3):

  #keep track of current position in each list
  i1, i2, i3 = 0,0,0 #start at the front
  #merge sorted 1 and 2 into 3
  n1,n2 = len(lst1), len(lst2)

  #loop while both 1 and 2 have more items
  while i1 < n1  and i2 < n2:
    if lst1[i1] < lst2[i2]:
      lst3[i3] = lst1[i1]
      i1 +=1
    else:
      lst3[i3] = lst2[i2]
      i2 +=1
    i3 += 1
  
  #if either list is done finish the merge
  #lst1
  while i1 < n1:
    lst3[i3] = lst1[i1]
    i1 += 1
    i3 += 1
  #lst2
  while i2< n2:
    lst3[i3] = lst2[i2]
    i2 += 1
    i3 += 1

def mergeSort(nums):
  #put items into a sorted list
  n= len(nums)
  #do nothing if 0 or 1 items
  if n > 1:
    #split into tow sublists
    m = n//2
    nums1, nums2 = nums[:m], nums[m:]
    #recursively sort each piece
    mergeSort(nums1)
    mergeSort(nums2)
    #merge the sorted pieces back into the list
    merge(nums1, nums2, nums)

def main():
  malist = [4,5,2,7,8,1,3]
  selSort(malist)
  print(malist)
  madlist = [3,1,4,1,5,9,2,6]
  mergeSort(madlist)
  print(madlist)
main()