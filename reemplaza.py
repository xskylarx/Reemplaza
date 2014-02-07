__author__ = 'soporte'
# Librerias Utilizadas
import re
import os
import glob
import sys

root = '/appCM/web'


#Configuracion, palabras a reemplazar

Cadena_1 = 'retaila' # Original
Cadena_1_r = 'jsandoval' # Reemplazo

Cadena_2 = 'at2dale' # Original
Cadena_2_r = 'karolanga' # Reemplazo

# Escribir tantas cadenas se quiera reemplazar en forma de Diccionario
reemplazo = {Cadena_1:Cadena_1_r,
           Cadena_2:Cadena_2_r}

def ruta_archivo():
    if root != None:
        Archivo = []
        for base, dirs, files in os.walk(root):
            for archivo in files:
                if '.php' in archivo:
                    Archivo.append(base + '/' + archivo)
        return  Archivo

# Archivo el cual se buscara las palabras y se reemplazaran
archivo = ruta_archivo()

# Crea un archivo nuevo con las palabras reemplazadas
def creaInicial(nombre):
    t=open(nombre,"w")
    t.close()

# Escribe el archivo ya reemplazado
def escribe(cadena):
    t=open("remplazo.txt","a")
    t.write(cadena + ' \n')
    t.close()

 # Borra el archivo Original
def BorraArchivo(archivo):
    try:

        for fl in glob.glob(archivo):
            print (fl)
            os.remove(fl)
    except Exception as m:
        print ('Archivo en Uso' + str(m))


def Remplaza_Cadena():
    for archivo_o in archivo:
        # Abre el archivo original y lo examina linea por linea
        archi=open(archivo_o,"r")
        lineas=archi.readlines()
        status = 0
        for li in lineas:
            cadena = li

            # Busca las palabras y las reemplaza
            regex = re.compile('(%s)' % '|'.join(map(re.escape, reemplazo.keys())))
            nueva_cadena = regex.sub(lambda x: str(reemplazo[x.string[x.start() :x.end()]]), cadena)

            # si la busqueda encuentra la palabra reemplazada en la variable, entonces escribe el nuevo contenido
            # de lo contrario escribe la cadena original

            if Cadena_1_r in nueva_cadena or Cadena_2_r in nueva_cadena:
                escribe (nueva_cadena.strip('\n'))
                status = 1
            else:

                escribe (cadena.strip('\n'))
        archi.close()
        if status == 1:
            Escribe_Log('Remplace ' + str(archivo_o))
        # Se elimina e archivo original
        BorraArchivo(archivo_o)

        # se renombra archivo de remplazo al nombre original
        os.rename('remplazo.txt',archivo_o)
        creaInicial('remplazo.txt')
    BorraArchivo('remplazo.txt')


def Lista_cadena():
    for archivo_o in archivo:
        print archivo_o
        archi=open(archivo_o,"r")
        lineas=archi.readlines()
        for li in lineas:
            cadena = li

            if Cadena_1 in cadena:
                Escribe_Log('Liste : ' + archivo_o)
        archi.close()




def Escribe_Log(archivo):
    try:
        t=open("remplaza.log","a")
        t.write( archivo + '  \n')
        t.close()
    except:
        print('Error al grabar log')
# Llama a la funcion para crear el archivo de reemplazo

creaInicial('remplaza.log')
opcion = raw_input('Listar Archivos  (L) Remplaza Archivos (R)')

if opcion.upper() == 'L':
    Lista_cadena()
else:
    Remplaza_Cadena()