import artistgraph as AG
import centrality as CT
from Tkinter import *
import json
from networkx.readwrite import json_graph
import tkFileDialog
import ntpath

## Function -------------------------------------------------------------------
currentGraphFilename = ""

def generateAndSave_graph():

    if( byType.get() == "ByGenre" ):
        ## Crear Grapho de Artistas por Genero ------------------------------------##
        genreName = nameEntry.get()
        limitSearch = limitEntry.get()
        G = AG.graphByGenre( genreName , int( limitSearch ) )

    elif( byType.get() == "ByArtist" ):
        ## Crear Grapho de Artistas ------------------------------------##
        artistName = nameEntry.get()
        depthSearch = limitEntry.get()
        G = AG.graphByArtist( artistName , int( depthSearch ) )
    
    ## Get Save Name
    fileName = tkFileDialog.asksaveasfilename( defaultextension = ".json")

    # write json formatted data
    d = json_graph.node_link_data(G) # node-link format to serialize
    # write json
    json.dump(d, open( fileName ,'w'))

    global currentGraphFilename
    currentGraphFilename = fileName
    
    currentLabel["text"] =  ntpath.basename(fileName)

    show_graph()

def open_graph():
    ## Get Save Name
    fileName = tkFileDialog.askopenfilename() 

    currentLabel["text"] =  ntpath.basename(fileName)   
    
    global currentGraphFilename
    currentGraphFilename = fileName

def show_graph():
    global currentGraphFilename

    ## load json formatted data
    json_data=open( currentGraphFilename )
    data = json.load( json_data )

    ## Create Graph from data
    G = json_graph.node_link_graph( data )

    if( centralityType.get() == "Degree" ):
        CentralMeasure = CT.centrality_degree( G )
    
    elif( centralityType.get() == "Closeness" ):
        CentralMeasure = CT.centrality_closeness( G )
    
    elif( centralityType.get() == "Betweenness" ):
        CentralMeasure = CT.centrality_betweenness( G )
    
    elif( centralityType.get() == "Eigenvector" ):
        CentralMeasure = CT.centrality_eigenvector( G )

    ## Dibujar Grafo con Medida de Centralidad
    CT.centrality_drawGraph( G , CentralMeasure )

def central_graph():
    global currentGraphFilename

    ## load json formatted data
    json_data=open( currentGraphFilename )
    data = json.load( json_data )

    ## Create Graph from data
    G = json_graph.node_link_graph( data )

    if( centralityType.get() == "Degree" ):
        CentralMeasure = CT.centrality_degree( G )
    
    elif( centralityType.get() == "Closeness" ):
        CentralMeasure = CT.centrality_closeness( G )
    
    elif( centralityType.get() == "Betweenness" ):
        CentralMeasure = CT.centrality_betweenness( G )
    
    elif( centralityType.get() == "Eigenvector" ):
        CentralMeasure = CT.centrality_eigenvector( G )

    ## Dibujar Grafo con Medida de Centralidad
    CT.centrality_centralNode( G , CentralMeasure , 10 )

## -----------------------------------------------------------------------------


## Gui Code ----------------------------------------------------##

## Initialization
master = Tk()
master.title( "ArtistGraph" )


byType = StringVar(master)
byType.set("ByGenre")

centralityType = StringVar(master)
centralityType.set("Degree")

currentGraphLabel = Label(master, text="Current Graph" )
currentGraphLabel.grid( row = 0 )

currentLabel = Label(master, text="None" , relief= "sunken" )
currentLabel.grid( row = 0 , column = 1 )

## Generating Graph Frame ------------------------------------------------------------------- 
OptionMenu(master, byType, "ByGenre", "ByArtist" ).grid( row = 1 , column = 1 )

graphLabel = Label(master, text="Graph" ).grid( row = 1 )
nameLabel  = Label(master, text="Name").grid( row = 2 )
limitLabel = Label(master, text="Limit \ Depth").grid( row = 3 )

nameEntry = Entry(master)
nameEntry.grid(row=2, column=1)

limitEntry = Entry(master)
limitEntry.grid(row=3, column=1)

OptionMenu(master, centralityType, "Degree" , "Closeness", "Betweenness", "Eigenvector" ).grid( row = 4 , column = 1)
centralityLabel = Label(master, text="Centrality" ).grid( row = 4)

Button(master, text='Generate & Save' , command = generateAndSave_graph ).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Open File', command= open_graph ).grid(row=5, column=1, sticky=W, pady=4)
Button(master, text='Draw Current', command=show_graph ).grid(row=6, column=0, sticky=W, pady=4)
Button(master, text='Show Central', command=central_graph ).grid(row=6, column=1, sticky=W, pady=4)

mainloop( )

## -----------------------------------------------------------------------------------------##

