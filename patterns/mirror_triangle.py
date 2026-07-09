n = int(input())
for i in range(n+1):

    s = " " * (n - i)
    symbol = "*" * i
    print(s + symbol)
"""
if n=5
output:
    *
   **
  ***
 ****
*****
"""