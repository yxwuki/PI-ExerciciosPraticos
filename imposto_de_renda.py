rendaAnual = float(input())

if rendaAnual <= 22847.76: 
    aliquota = 0
    parcela = 0
elif rendaAnual >= 22847.77 and rendaAnual <= 33919.80:
    aliquota = 0.075
    parcela = 1713.58
elif rendaAnual >= 33919.81 and rendaAnual <= 45012.60:
    aliquota = 0.15
    parcela = 4257.57
elif rendaAnual >= 45012.61 and rendaAnual <= 55976.16:
    aliquota = 0.225
    parcela = 7633.51
else: 
    aliquota = 0.275
    parcela = 10432.32

impPago = rendaAnual * aliquota - parcela

aliqEfetiva = (impPago/rendaAnual)*100

print("%.2f" % aliqEfetiva)
