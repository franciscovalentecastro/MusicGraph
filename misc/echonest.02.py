import networkx as nx
import matplotlib.pyplot as plt
import math

## PyEchonest ---------------------------------------------
from pyechonest import config
from pyechonest import artist

config.ECHO_NEST_API_KEY="JEXRSXP8AZST5QCNP"
## --------------------------------------------------------

## PyEn ---------------------------------------------------
import pyen
en = pyen.Pyen("JEXRSXP8AZST5QCNP")
## --------------------------------------------------------

## Funciones ---------------------------------------------------##

def getArtistByGenre( genre , limit ):
	result = artist.search( style = genre , results = limit , sort='familiarity-desc' )
	listArtist = []

	for artist_result in result:
            listArtist.append( ( artist_result.name , artist_result.id  ) )

	return listArtist

def relatedArtist( artist_id ):
    
    listArtist = []

    ##try:
    bk = artist.Artist( artist_id )
    ##except WebServiceError as exc:
    ##    print("Something went wrong with the request: %s" % exc)
    ##else:
        
    for similar_artist in bk.similar:            
        listArtist.append( ( similar_artist.name ,  similar_artist.id  ,  "similar" ) )

    return listArtist

## --------------------------------------------------------------##

##getArtistByGenre( 'blues' , 25 )

## Crear Grapho de Artistas ------------------------------------##
##artistName = raw_input('Artist Name: ')
##G = graphByArtist( artistName , 2 )


## Dibujar grafica --------------------------------------------##
##nx.draw(G,pos=nx.spring_layout(G), nodecolor='r',edge_color='b', with_labels=True)
##plt.show()





