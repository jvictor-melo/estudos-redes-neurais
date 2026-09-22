# Preciso colocar os seguintes dados e calculos:
# Pesos: w(0) = [], Valor Inicial: x(0) = [], theta = Number, 
# eta = Number, valor desejado: d = Number, Epocas: Number
# Calculo do disparo: u(epoca) = w0x0 + w1x1 + ...
# Função sinal: u >= 0 => y = 1, u < 0 => y = -1
# Calculo erro: e = d - y. 
# e = 0 => Cabou 
# e > ou < 0 => Continua
# Alterar Pesos: w(epoca + 1) = w(epoca) + eta * e * x

import numpy as np

valor_inicial = np.array([[0, 0], [1, 0], [0, 1], [1, 1]]) # x
N, p = valor_inicial.shape
valor_inicial_bias = np.hstack([-np.ones((N, 1)), valor_inicial])

pesos = np.zeros(p + 1) # w, incluindo theta, e zerando todos os pesos

valor_desejado = np.array([-1, 1, 1, 1]) # d
eta = 0.5 # taxa de aprendizado
epocas = 20

for i in range(epocas):
    print("\n****************************")
    print(f"\nEstamos na Tentativa: {i}\n")
    print("****************************\n")

    erros_na_epoca = 0

    for t, linha in enumerate(valor_inicial_bias):
        soma = np.dot(pesos, linha)

        if soma >= 0:
            y = 1
        else:
            y = -1

        erro = valor_desejado[t] - y
        print(f"U={soma}, y={y}, erro={erro}")

        if erro != 0:
            erros_na_epoca += 1
            pesos = pesos + eta * erro * linha
            print(f"novos pesos:\n {pesos}\n")
        else:
            pass

    if erros_na_epoca == 0:     
        print(f"\nConvergiu na epoca {i+1}")
        break


#! FAZENDO SEM NUMPY

# for i in range(epocas):
#     print("\n****************************")
#     print(f"\nEstamos na Tentativa: {i}\n")
#     print("****************************\n")
#     erros_na_epoca = 0
#     for t, linha in enumerate(valor_inicial):
#         soma = 0
#         for j in range(len(pesos)):
#             soma += pesos[j] * linha[j]
#         if soma >= 0:
#             y = 1
#         else:
#             y = -1
#         erro = valor_desejado[t] - y
#         print(f"U={soma}, y={y}, erro={erro}")
#         if erro != 0:
#             erros_na_epoca += 1
#             for k in range(len(pesos)):
#                 pesos[k] = pesos[k] + (eta * erro * linha[k])
#             print(f"novos pesos:\n {pesos}\n")
#         else:
#             pass
#     if erros_na_epoca == 0:     
#         print(f"\nConvergiu na epoca {i+1}")
#         break


