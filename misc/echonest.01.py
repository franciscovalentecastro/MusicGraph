import networkx as nx
import matplotlib.pyplot as plt
import math

from pyechonest import config
from pyechonest import artist

config.ECHO_NEST_API_KEY="JEXRSXP8AZST5QCNP"

## Funciones ---------------------------------------------------##

def getArtistByGenre( genre , limit ):
	result = artist.search( style = genre , results = limit , sort='familiarity-desc' )
	listArtist = []

	for artist_result in result:
            listArtist.append( str( artist_result.get_foreign_id( idspace='musicbrainz').replace('musicbrainz:artist:', '') ) )

	return listArtist

def recursiveGraph( G , tempName , depth ):
	if depth == 0:
		return 


	bk = artist.Artist( tempName )
	G.add_node( bk.name )
	
	for similar_artist in bk.similar: 
		G.add_node( similar_artist.name )
		G.add_edge( similar_artist.name , bk.name )
		recursiveGraph( G , similar_artist.name , depth - 1 )


def graphByArtist( artistName , depth ):

	G = nx.Graph()
	recursiveGraph( G , artistName , depth )

	return G

## --------------------------------------------------------------##

##getArtistByGenre( 'blues' , 25 )

## Crear Grapho de Artistas ------------------------------------##
##artistName = raw_input('Artist Name: ')
##G = graphByArtist( artistName , 2 )


## Dibujar grafica --------------------------------------------##
##nx.draw(G,pos=nx.spring_layout(G), nodecolor='r',edge_color='b', with_labels=True)
##plt.show()





