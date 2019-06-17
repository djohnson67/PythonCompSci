from math import sqrt

def getNumbers():
    nums = []
    # sentinel loop to get numbers
    inputString = 'Enter a number (<Enter> to quit) >> '
    xStr = input(inputString)
    while xStr != '':
        x = eval(xStr)
        nums.append(x) # add x to nums list
        xStr = input(inputString)
    return nums

#compute the mean from a list
def mean(nums):
    sum = 0.0
    for num in nums:
        sum = sum + num
    return sum / len(nums)
#compute the standard deviation from a list
def stdDev(nums, xbar):
    sumDevSq = 0.0
    for num in nums:
        dev = num - xbar
        sumDevSq  = sumDevSq + dev * dev
    return sqrt(sumDevSq/len(nums)-1)

#compute the median from a list
def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        median = (nums[midPos] + nums[midPos - 1]) / 2
    else:
        median = nums[midPos]
    return median

def main():
    print('This program computes the mean, median, and standard deviation.')

    data = getNumbers()
    xBar = mean(data)
    std = stdDev(data, xBar)
    med = median(data)

    print('The mean is',xBar)
    print('The median is',med)
    print('The standard deviation is',std)


if __name__ == '__main__': main()