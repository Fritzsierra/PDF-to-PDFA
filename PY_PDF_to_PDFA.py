
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 23:45:35 2019

@author: fsierra
"""

import fitz
import os
import getpass
from datetime import datetime
import sys
import PySimpleGUI as sg

#MENSAJE INICIAL
sg.theme('DarkPurple5')
layout=[[sg.Text('RECOMENDACIONES ANTES DE INICIAR:\n\n 1. En la carpeta deben estar los archivos "PDFs" para ser convertidos a "PDFA". \n\n 2. En la carpeta debe estar el archivo "PDFA.pdf" necesario para convertir los demás archivos a PDFA.  \n\n Deseas continuar?')],
     [sg.Button('SI'), sg.Button('NO')]]
window= sg.Window('PY-PDFA', layout)
event, values = window.read()
window.close()

try:
    if event=="SI":
        
        username = getpass.getuser().upper()                        #USUARIO DE PC
        now = datetime.now().strftime("%d-%m-%Y %H-%M-%S")          #FECHA Y HORA ACTUAL
        path= os.getcwd()                                           #CARPETA ACTUAL
        resultado='RESULTADO'+'_'+username+'_'+now                  #CREAMOS EL NOMBRE DE LA CARPETA DE RESULTADO
        os.makedirs(resultado)                                      #CREAMOS LA CARPETA RESULTADO
        documentos=os.listdir(path)                                 #LISTAMOS LOS ARCHIVOS DE LA CARPETA
        documentos = [k for k in documentos if '.pdf' in k]         #FILTRAMOS LOS ARCHIVOS QUE SEAN PDF
        documentos = [k for k in documentos if 'PDFA.pdf' not in k] #FILTRAMOS LOS ARCHIVOS PDF Y QUE NO SEA PDFA
            
        
        for i in documentos:    
            pdfa= fitz.open(path+"\\PDFA.pdf")                      #ABRIAMOS EL ARCHIVO PDFA EN BLANCO
            documento = fitz.open(path+"\\"+i)                      #ABRIMOS EL ACHIVO PDF
            pdfa.insertPDF(documento)                               #INSERTAMOS(MERGE) EL ARCHIVO PDFA EN BLANCO CON EL ARCHIVO PDF 
            pdfa.deletePage(0)                                      #ELIMINAMOS LA PRIMERA HOJA DLE ARCHIVO PDFA EN BLANCO
            pdfa.save(path+"\\"+resultado+"\\"+i)                   #GUARDAMOS EL NUEVO ARCHIVO PDFA EN LA CARPETA RESULTADO
            pdfa.close()                                            #CERRAMOS EL PDFA
            documento.close()                                       #CERRAMOS EL ARCHIVO PDF
            os.remove(path+"\\"+i)                                  #ELIMINAMOS EL ARCHIVO PDF
                    
        #MENSAJE FINAL
        sg.theme('DarkPurple')
        layout = [ [sg.Text('El proceso ha terminado exitosamente')],
                    [sg.Button('Ok')]]
        window = sg.Window('PY-PDFA', layout)
        event, valor = window.read()
        window.close() 

    sg.theme('DarkPurple')
    layout = [ [sg.Text('Has decido no ejecutar el PY-PDFA.')],
                [sg.Button('Ok')]]
    window = sg.Window('PY-PDFA', layout)
    event, valor = window.read()
    window.close() 

except:
    sg.theme('DarkRed1')
    layout = [ [sg.Text('Ha ocurrido un ERROR!!! en el proceso del PY-PDFA.')],
                [sg.Button('Ok')]]
    window = sg.Window('PY-PDFA', layout)
    event, valor = window.read()
    window.close()
    sys.exit()












