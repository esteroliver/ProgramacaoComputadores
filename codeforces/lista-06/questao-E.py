def dia_da_semana(h,d):
    dias = ['Domingo','Segunda-feira','Terca-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sabado']
    ind_dia = (dias.index(h)+d)%7
    return dias[ind_dia]
            
