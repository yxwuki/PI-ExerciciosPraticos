# entrada dos horários
entra = input()
saida = input()

# separação por listas das horas e dos minutos HH:MM
entraLista = entra.split(':')
saidaLista = saida.split(':')

# identificação das horas e minutos nos horários
entraHora = int(float(entraLista[0]))
entraMin = int(float(entraLista[1]))

saidaHora = int(float(saidaLista[0]))
saidaMin = int(float(saidaLista[1]))

# conversão horas em minutos + soma dos minutos
entraTempo = entraHora * 60 + entraMin
saidaTempo = saidaHora * 60 + saidaMin

# tempo de uso do estacionamento 
tempo = saidaTempo - entraTempo

# transformação minutos em horas
horas = 0
while tempo >= 60:
    tempo = tempo - 60
    horas = horas + 1 

# sobra de minutos
if tempo <= 15 and tempo > 0 and horas == 0:
    horas = 0
elif tempo > 0:
    horas = horas + 1

# calculo das horas pra pagar
if horas == 0: 
    pagar = 0
elif horas > 0 and horas <= 1:
    pagar = 5
elif horas >= 2 and horas <= 4:
    pagar = (horas - 1) * 3 + 5
elif horas >= 5:
    pagar = (horas - 4) * 2 + 14

print("R$ %.2f" % pagar)
