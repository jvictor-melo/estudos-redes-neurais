# Preciso colocar os seguintes dados e calculos:
# Pesos: w(0) = [], Valor Inicial: x(0) = [], theta = Number, 
# alpha = Number, valor desejado: d = Number, Epocas: Number
# Calculo do disparo: u(epoca) = w0x0 + w1x1 + ...
# Calculo erro: e = d - u. 
# e = 0 => Cabou 
# e > ou < 0 => Continua
# Alterar Pesos: w(epoca + 1) = w(epoca) + alpha * e * x

teta = 1
pesos = [teta, -3, -2] # w
valor_inicial = [[-1, 0, 0], [-1, 1, 0], [-1, 0, 1], [-1, 1, 1]] # x
valor_desejado = [-1, 1, 1, 1] # d
alpha = 0.5 # taxa de aprendizado
epocas = 20


for i in range(epocas):
    print("\n****************************")
    print(f"\nEstamos na Tentativa: {i}\n")
    print("****************************\n")
    erros_na_epoca = 0
    for t, linha in enumerate(valor_inicial):
        soma = 0
        for j in range(len(pesos)):
            soma += pesos[j] * linha[j]
        erro = valor_desejado[t] - soma
        print(f"U={soma}, erro={erro}")
        if erro != 0:
            erros_na_epoca += 1
            for k in range(len(pesos)):
                pesos[k] = pesos[k] + (alpha * erro * linha[k])
            print(f"novos pesos:\n {pesos}\n")
        else:
            pass
    if erros_na_epoca == 0:     
        print(f"\nConvergiu na epoca {i+1}")
        break


