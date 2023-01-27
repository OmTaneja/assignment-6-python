num = int(input("Enter number of rows of pascals triangle :-"))

def pascals_tri(n):
   nth = [1]
   a = [0]
   for x in range(max(n,0)):
      print(" "*(n-x) , nth)
      nth=[b+c for b,c in zip(nth +a , a+nth)]
   return n>=1


pascals_tri(num)