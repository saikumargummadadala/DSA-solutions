n = int(input())
for i in range(n,-1,-1 ):
    s = " " * (n - i)
    symbol = "*" * (2 * i - 1)
    print(s + symbol)
"""
if n=5
output:
*********
 *******
  *****
   ***
    *
    """
