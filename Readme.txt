ArtistGraph - Readme
La aplicación fue hecha y probada para ejecutarse en "Python 2.7.8" y depende de las siguientes librerias 
( que pueden ser instaladas sin ningun problema con la aplicación "pip" para instalar librerias de python ) :

-musicbrainzngs
-pyechonest
-pyen
-networkx
-matplotlib
-tkinter
-json
-numpy
-scipy

El archivo python que debe ser ejecutado es "main_app.py" . La aplicación cuenta con una interfaz gráfica
sencilla de utilizar. 

Se debe escoger el tipo de grafo a generar : Por "Genero" ó "Artista".
Luego en el campo se debe poner el nombre del artista ó el genero.
-Si es por "Genero" se debe poner un limite entre 1 y 15 para generar el grafo.
-Si es por "Artista" hay que poner el limite de la profundidad del grafo a generar ( No hay limite :P ).

Despues se debe escoger la medida de centralidad a utilizar.

La opción "Generar y Guardar" genera un grafo con las opciones descritas anteriormente y lo guarda en la ruta especificada.
La opción "Abrir Archivo" nos deja escoger el grafo con el que trabajar sin tener que generarlo desde un archivo ".json".

Al final tenemos las opciones de mostar el grafo con la medida de centralidad especificada ó imprimir en consola a los 
10 primeros artistas con mayor medida de centralidad en orden con su valor de medida.
