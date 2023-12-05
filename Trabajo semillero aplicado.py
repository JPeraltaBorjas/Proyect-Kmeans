#!/usr/bin/env python
# coding: utf-8

# In[7]:


# K-Means Clustering

# Importacion de librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

def new_list(X): #FUNCION PARA DEVOLVER LA MISMA LISTA SIN DATOS ATÍPICOS
    
    p25 = np.quantile(X, 0.25) #Te devuelve el cuartil 1 de una lista
    p75 = np.quantile(X, 0.75) #Te devuelve el cuartil 3 de una lista
    inter_rang = p75-p25 #Calcula el rango intercuantil
    maximo = p75+(1.5*inter_rang) #Calcula el maximo de los datos a escoger

    n = len(X) #Numero de elementos de la lista
    eleg = []

    for i in range (n):
        if(X[i] != 0 and X[i]<=maximo):
            eleg.append(X[i]) #Agrega a la lista vacia elementos FUERA DE LOS ATIPICOS
    eleg.sort() #Ordena la lista
    #print(eleg)
    return(eleg) #Retorna una lista


# In[5]:


def kmedias(X,Y,Z):
    
    print("------------------------------------------------------------------")
    if X == []:
        print("No hay datos a graficar en {}: {}".format(Y,Z))
    else:    
        wcss = []
        for i in range(2, 11):
#             kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
            kmeans = KMeans(n_clusters = i, max_iter = 10)
            kmeans.fit(X)
            wcss.append((kmeans.inertia_)/len(X))
#         print(wcss)  
        for i in range(9):
            print('K = {} -> {:.2f}'.format(i+2, wcss[i]))
            
        # Grafica de la suma de las distancias
        plt.plot(range(2,11),wcss,'.-')
        plt.title('{}: {}'.format(Y,Z))
        plt.xlabel('Number of clusters')
        plt.ylabel('WCSS')
        plt.grid()
        plt.show()


# In[ ]:



base = input('Ingrese nombre la base de datos por segmentación (en mayuscula): ')
base = base + '.xlsx'
print('En {}, se encuentran las pestañas:'.format(base))

nom_pest = pd.ExcelFile(base).sheet_names #Pone los nombres de las pestañas del excel en una lista
# print(nom_pest[5])
n = len(nom_pest)
# print(n)

for i in range (n):
    print('  {}. {}'.format(i+1,nom_pest[i]))

elec = int(input('Elija una pestaña para la grafica por el metodo del codo, para que se grafiquen todo otro numero: '))
elec = elec-1

if elec >=0 and elec < n:
    dataset = pd.read_excel(base, sheet_name = nom_pest[elec])
    Y = ['Número de Débitos', 'Suma de Débitos', 'Número de Créditos', 'Suma de Créditos']
    
    for i in range (4):
        X = dataset.iloc[:,[i]].values
        kmedias(new_list(X),nom_pest[elec],Y[i])
else:
#     elem=[]
    for i in range (n):
#         dataset = 0
        print("\n\nCATEGORIA - {}".format(nom_pest[i]))
        dataset = pd.read_excel(base, sheet_name = nom_pest[i])
        for j in range (4):
            X = dataset.iloc[:,[j]].values
            kmedias(new_list(X),nom_pest[i],Y[j])
#         elem.append(dataset
#     print(elem)

