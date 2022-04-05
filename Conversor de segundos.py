''' No código abaixo ele irá configurar qualquer número que você digite para segundos '''

numerodesegundos = int(input("Por favor, entre com o número 
                       " de segundos que deseja converter: "))
dias = numerodesegundos//86400
segundosrestan = numerodesegundos % 86400
horas = segundosrestan // 3600
segundrestodossegun = segundosrestan % 3600
minutos = segundrestodossegun // 60
restsegunfinal = segundrestodossegun % 60
print(dias, "dias,", horas, "horas,", minutos, "minutos e",
      restsegunfinal, "segundos.")
