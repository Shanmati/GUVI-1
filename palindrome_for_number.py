n=int(input())
rev=0
temp=n

if(n<=1000):
  while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(rev==temp):
  print('yes')
else:
  print('no')
