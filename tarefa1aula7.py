lampadas= float(input('quamtas lampadas incandecentes vc ultiliza?'))
tempolampada= float(input('quanto tempo sua lamapada fica ligada?'))
wattslampadas= float(input('quantos watts ultiliza sua lampada?'))


def calcular_economia(economia):
    dia= (lampadas * tempolampada) * wattslampadas
    diaLED= dia * 0.80 
    mes= dia * 31
    mesLED= mes * 0.80
    ano= dia * 365
    anoLED= ano * 0.80
    return diaLED, mesLED, anoLED



#print('com lampadas de LED ultilizará {0:.2f}watts por dia.' .format(diaLED))
#print('com lampadas de LED ultilizará {0:.2f}watts em um mês.' .format(mesLED))
#print('com lampadas de LED ultilizará {0:.2f}watts em um ano.' .format(anoLED))