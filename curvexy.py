import numpy as np

# Definindo as funções da curva
def gamma_x(t):
    return 5 * np.cos(t) - 4 * np.cos(5 * t / 2)

def gamma_y(t):
    return 5 * np.sin(t) - 4 * np.sin(5 * t / 2)

def filtrar_lista(lista, limite=0.1):
    nova_lista = [lista[0]]  # Começa com o primeiro elemento
    for i in range(1, len(lista)):
        if abs(lista[i] - lista[i - 1]) >= limite:
            nova_lista.append(lista[i])
    return nova_lista

# Intervalos de t para busca de soluções
t_values = np.linspace(0, 4 * np.pi, 2000)  # Aumentando o número de amostras para maior precisão

intersectionst1 = []
intersectionst2 = []

for t1 in t_values:
    for t2 in t_values:
        if ((gamma_x(t1)-gamma_x(t2)<0.03) and (gamma_x(t1)-gamma_x(t2)>-0.03)):
              if (gamma_y(t1)-gamma_y(t2)<0.03) and (gamma_y(t1)-gamma_y(t2)>-0.03):
                    if (t1-t2>0.5) or (t2-t1>0.5):
                        if t1 not in intersectionst1:
                            intersectionst1.append(t1)
                        if t2 not in intersectionst2:
                            intersectionst2.append(t2)
                        
intersectionst1 = filtrar_lista(intersectionst1)
intersectionst2 = filtrar_lista(intersectionst2)

for i in (range(len(intersectionst1)-1)):
    print("intersec em t1: "+ str(intersectionst1[i]) + ", t2: " + str(intersectionst2[i]))

print("\n achei: " + str(len(intersectionst2)) + " valores de t1's e t2's")