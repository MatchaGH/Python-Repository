nome = input ("digite seu nome: ")
idade = input ("me diga sua idade: ")

if nome and idade : 
    print (f"seu nome é {nome}")
    print (f"seu nome invertido é {nome[::-1]}")

    if " " in nome:
        print ("seu nome contém espaços")
    else: 
        print ("seu nome não contém espaços")

    print (f"seu nome contém {len(nome)} letras")
    print (f"a primeira letra do seu nome é {nome[0]}")
    print (f"a última letra do seu nome é {nome[-1]}")

else:
    print ("Voce deixou campos vazios")