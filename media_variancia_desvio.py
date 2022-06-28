x1 = float(input())
x2 = float(input())
x3 = float(input())
x4 = float(input())

media = (x1+x2+x3+x4)/4
v = ((x1-media)**2+(x2-media)**2+(x3-media)**2+(x4-media)**2)/3
dp = (v)**(1/2)

print("media = %.2f" %media)
print("variancia = %.2f"%v)
print("desvio = %.2f" %dp)
