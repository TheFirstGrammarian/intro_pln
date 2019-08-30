#El siguiente programa toma una serie de oraciones, y nos devuelve un archivo con esas oraciones y su POS-tags.
#MFNT - 2019

import pickle
import nltk
from nltk.tokenize import word_tokenize

NaiveBayesTagger = pickle.load(open("/content/drive/My Drive/Colab Notebooks/NaiveBayesTagger.p", "rb"))#Abrimos nuestro POS-tagger ya entrenado

#Vamos a definir la función analizadora, que toma una oración, la tokeniza, y luego le asigna a cada token su POS-tag
def analizar(oracion):
    return(NaiveBayesTagger.tag(word_tokenize(oracion)))


oraciones_analizadas = [] #Declaramos una lista vacía en donde guardaremos nuestros análisis
nombre = (input("Yo soy Gramaticon-3000, tu asistente personal para el análisis de oraciones. ¿Cuál es tú nombre?: ")).capitalize() #pedimos el nombre del usuario
analisis = (input("Hola " + nombre + ", ¿deseas comenzar el análisis de oraciones? (si/no): ")).lower() #le preguntamos si quiere analizar una oración

while True:
    if analisis == 'si': #Si el usuario quiere analizar una oración
        oracion = input("¿Qué oración te gustaría analizar?:\n") #le preguntamos cuál es su oración
        oraciones_analizadas.append(analizar(oracion)) #la analizamos con nuestra función ya definida y la guardamos en nuestra lista
        analisis = input("\nTe gustaría analizar otra oración? (si/no): ") #y le preguntamos si quiere analizar otra oración.
    elif analisis == 'no': #si el usuario no quiere analizar una oración,
        print("\nBueno " + nombre + ", es una lástima que te vayas :(, ¡Espero verte pronto!\n") #nos despedimos
        break #y salimos del loop
    else: #Si el usuario no responde ni "si" ni "no", le pedimos que introduzca un valor válido.
        analisis = input("Has introducido un valor que no reconozco: \"" + analisis + "\". Inténtalo de nuevo (si/no): ")

#Imprimimos nuestro análisis
print("\nOraciones analizadas:\n" + str(oraciones_analizadas))
'''
#Guardamos nuestro análisis en un archivo txt
nombre_archivo = input("¿Con qué nombre quieres que guarde este archivo?: ") #Preguntamos el nombre del archivo
with open(+ nombre_archivo + '.txt', 'w') as file:
    analisis_completo = file.write(str(oraciones_analizadas)) #Guardamos el resulado del análisis

print("¡Éxitos! " + nombre_archivo + " ya fue guardado") #Imprimimos un mensaje final
'''
