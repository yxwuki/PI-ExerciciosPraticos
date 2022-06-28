import math
conta = input().lower()
lc = conta.split(' ')
op = lc[0]
x = float(lc[1])
if len(lc)==3:
  y = float(lc[2])
else: 
  y = 0

if op == "sum":
    calc = x + y 
elif op == "dif":
    calc = x - y
elif op == "mult":
    calc = x * y 
elif op == "div": 
    calc = x / y
elif op == "pot": 
    calc = x ** y
elif op == "raiz":
    calc = x ** (1/2) 
elif op == "log10": 
    calc = math.log (x, 10)
print("%.2f" % calc)
