def dia(dia, mes, ano):
    meses = ['janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    
    if (mes <= 12 and mes > 0):

        if (mes in [1, 3, 5, 7, 8, 10, 12]):
            if (dia <= 31 and dia > 0):
                return "{:02d} de {} de {}".format(dia,meses[mes-1],ano)
            else: 
                return 'Data Invalida'
            
        elif (mes in [4, 6, 9, 11]):
            if (dia <= 30 and dia > 0):
                return "{:02d} de {} de {}".format(dia,meses[mes-1],ano)
            else: 
                return 'Data Invalida'
            
        elif (mes == 2):
            if (dia <= 28 and dia > 0):
                return "{:02d} de {} de {}".format(dia,meses[mes-1],ano)
            else: 
                return 'Data Invalida'
            
    else:
        return 'Data Invalida'