#!/usr/bin/env python
# coding: utf-8

# # Taller 2

# Xiomy Díaz Morales - Esp. Analítica Estratégica de datos

# ### Punto 1

# #### 1.1 Descomprimir archivo Zip

# In[52]:


import os
from zipfile import ZipFile


# In[53]:


direccion = "Desktop/archivos/poemas.zip"


# In[54]:


#Descomprimir el archivo
with ZipFile(direccion) as archivo:
    archivo.extractall("Desktop/archivos")


# Ver el nombre de los archivos

# In[55]:


for archivo in os.walk('archivos/poemas'):
    print(archivo)


# In[56]:


for raiz, dirs, archivos in os.walk('archivos/poemas'):
        for archivo in archivos:
            print(archivo)


# #### 1.2 Leer archivos

# In[69]:


# abrir archivo txt en python
with open ("Desktop/archivos/poemas/A un general (Julio Corta╠üzar).txt") as archivo:
    data1 = archivo.read()
    print ("texto1: ",data1)
    print("*"*100)
    print()
    
with open ("Desktop/archivos/poemas/Aqui╠ü (Octavio Paz).txt") as archivo:
    data2 = archivo.read()
    print ("texto2: ",data2) 
    print("*"*100)
    print()
    
with open ("Desktop/archivos/poemas/Si╠ündrome (Mario Benedetti).txt") as archivo:
    data3 = archivo.read()
    print ("texto3: ",data3)  
    print("*"*100)
    print()


# #### 1.3 ¿Cuál archivo tiene el mayor número de palabras?

# In[58]:


#Para contar palabras en un texto
import re
def countWords(fitxer):
    f = open(fitxer,"r")
    text = f.readlines()
    f.close()
    cont = 0
    for lines in text:
        found = re.findall("([a-z\']+)", lines.strip(), re.I)
        if found:
           cont += len(found)
    if cont > 1:
        return "El archivo tiene %s palabras" % cont
    elif cont == 0:
        return "El archivo esta vacio"
    else:
        return "El archivo tiene %s palabra" % cont
    



# In[59]:


countWords("Desktop/archivos/poemas/A un general (Julio Corta╠üzar).txt")


# In[60]:


countWords("Desktop/archivos/poemas/Aqui╠ü (Octavio Paz).txt")


# In[61]:


countWords("Desktop/archivos/poemas/Si╠ündrome (Mario Benedetti).txt")


# El archivo con más palabras es Si╠ündrome (Mario Benedetti).txt

# ### Punto 2

# #### 2.1 Web Scraping de 10 biografías en Wikipedia (en búcle)

# #### 2.2 Obtener el encabezado de cada biografía

# In[65]:


import urllib.request


# In[66]:


import bs4 as bs


# In[67]:


links = ["https://es.wikipedia.org/wiki/Carl_Sagan", "https://es.wikipedia.org/wiki/Nikola_Tesla",
        "https://es.wikipedia.org/wiki/Albert_Einstein","https://es.wikipedia.org/wiki/Alan_Turing",
        "https://es.wikipedia.org/wiki/William_Bradford_Shockley","https://es.wikipedia.org/wiki/Ramon_Llull",
        "https://es.wikipedia.org/wiki/Marvin_Minsky","https://es.wikipedia.org/wiki/Allen_Newell",
        "https://es.wikipedia.org/wiki/Herbert_Alexander_Simon","https://es.wikipedia.org/wiki/George_Boole"]


# In[68]:


for scraping in links:
    request = urllib.request.urlopen(scraping)
    source = request.read()
    request.close()
    soup = bs.BeautifulSoup(source,'html.parser') 
    print(soup.find('h1').text)  #Para obtener el encabezado


# #### 2.3 Obtener todos los contenidos y etiquetas de título asociados a los links del primer párrafo

# In[51]:


for scraping in links:
    request = urllib.request.urlopen(scraping)
    source = request.read()
    request.close()
    soup = bs.BeautifulSoup(source,'html.parser')
    print(soup.find('h1').text)
    for url in soup.find('p').find_all('a'): #obtener urls de los links del primer párrafo
        print (url)
        print ('Contenido:') #para cada url traer contenido y título
        print (url.contents)
        print ('Título:')
        print(url.get('title'))
    print("*"*100)
    print()

