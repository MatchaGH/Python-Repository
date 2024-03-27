horas = input('Que horas são? ')

try:
    horas_float = float(horas)

    if horas_float >= 6 and horas_float <= 12:
        print('bom dia flor do dia')
    elif horas_float >= 12.1 and horas_float <= 18:
        print('boa tarde filho da puta')
    elif horas_float >= 18.1 and horas_float <= 24:
        print('boa noite desgraça')
    elif horas_float >= 0 and horas_float <= 5.9:
        print('tu tinha era que ta dormindo infeliz')
    else:
        print('não conheço essa hora mano')
except:
    print('nem hora isso ai é arrombado')