resposta = str
resultado = 0
valores = []
while resposta != "NÃO": 
    resposta = str(input("Deseja realizar alguma operação hoje?\n")).strip().upper()
    if resposta == "NÃO":
         break
    
    operacao = int(input("Informe o tipo de operação que deseja realizar:\n1- ADIÇÃO\n2-SUBTRAÇÃO\n3-MULTIPLICAÇÃO\n4-DIVISÃO\n"))

    if operacao == 1:
        for n in range(2):
            n += 1
            n1 = float(input("Insira o {}º valor: ".format(n)))
            valores.append(n1)
        resultado = sum(valores)
        print(resultado)
        
    elif operacao == 2:
        for n in range(2):
            n += 1
            n1 = float(input("Insira o {}º valor: ".format(n)))
            valores.append(n1)
        resultado = valores[0] - valores[1]
        print(resultado)
        

    elif operacao == 3:
        for n in range(2):
            n += 1
            n1 = float(input("Insira o {}º valor: ".format(n)))
            valores.append(n1)
        resultado = valores[0] * valores[1]
        print(resultado)

    elif operacao == 4:
        for n in range(2):
            n += 1
            n1 = float(input("Insira o {}º valor: ".format(n)))
            valores.append(n1)
        resultado = valores[0] / valores[1]
        print(resultado)
        
print('FIM DO PROGRAMA')