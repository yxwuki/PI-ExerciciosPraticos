x = float(input())

cem = x//100
cemR = x%100
cinq = cemR//50
cinqR = cemR%50
vinte = cinqR//20
vinteR = cinqR%20
dez = vinteR//10
dezR = vinteR%10
cinco = dezR//5
cincoR = dezR%5
dois = cincoR//2
um = cincoR%2

print("Cédulas de R$ 100.00: %.0f" % cem, "\nCédulas de R$ 50.00: %.0f" % cinq, "\nCédulas de R$ 20.00: %.0f" % vinte, "\nCédulas de R$ 10.00: %.0f" % dez, "\nCédulas de R$ 5.00: %.0f" % cinco, "\nCédulas de R$ 2.00: %.0f" % dois, "\nCédulas de R$ 1.00: %.0f" % um)
