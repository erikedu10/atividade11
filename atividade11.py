dist = int(input("insira a distancia da sua viagem:"))

if dist < int("200"):
  print("o valor da sua passagem é:",float(dist*0.50))
else:
  print("o valor da sua passagem é:",float(dist*0.45))