data = input()

# separação e lista
dataSep = data.split('/')
dia = int(float(dataSep[0]))
mes = int(float(dataSep[1]))
ano = int(float(dataSep[2]))

# próximo dia
if dia == 31:
    dia = 1 
else:
    if dia == 30:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            dia = 1
        else: 
            dia = dia + 1
    elif dia == 28 and mes == 2:
        dia = 1
    else: 
        dia = dia + 1

# próximo mes
if dia == 1 and mes != 12:
    mes = mes + 1
elif mes == 12: 
    mes = 1
elif dia == 28 and mes == 2:
    mes = 3 
else: 
    mes = mes

#proximo ano 
if dia == 1 and mes == 1:
    ano = ano + 1
else: 
    ano = ano

print("%.2d/%.2d/%.2d" % (dia,mes,ano))
