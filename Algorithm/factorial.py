def fact(n):
    if n == 0:
        return 1;
    else:
        return n * fact(n-1)

def reverse(s):
    if s =='':
        return s
    else:
        temp = reverse(s[1:]) + s[0]
        #print (temp)
        return temp

def anagarams(s):
    if s == '':
        return [s]
    else:
        ans = []
        for w in anagarams(s[1:]):
            for pos in range(len(w)+1):
                print(w[:pos] + s[0] + w[pos:])
                ans.append(w[:pos] + s[0] + w[pos:])
        return ans

def loopPower(a, n):
  ans = 1;
  for i in range(n):
    ans *= a
  return ans

#divide and conquer algorythm
def recPower(a,n):
  #raises a to the nth power
  if n == 0:
    return 1
  else:
    factor = recPower(a,n//2)
    if n%2 == 0: #n is even
      return factor * factor
    else: #n is odd
      return factor * factor * a

def main():
  res = fact(6)
  print('And the result is', res)
  red = reverse('Hello')
  print('Hello backwards is: ', red)
  anag = anagarams('abc')
  print (anag)
  ans = recPower(3,5)
  print( '3^5 = ', ans)

def loopfib(n):
  #returns  the nth fibonacci number
  curr = 1
  prev = 1
  for i in range(n-2):
    curr, prev = curr+prev, curr
  return curr

main()


  