minuto = 30
hora = 2
for i in range(100):
    minuto += 1
  
    if minuto > 59:
                hora +=1
                minuto = 0
    print("Hora",hora, "minuto", minuto)
    
