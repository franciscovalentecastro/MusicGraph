import networkx as nx
import matplotlib.pyplot as plt
import echonest as en
import musicbrainz as mz
import math

## Initilization -----------------------------------------------------------------------
DefaultWeight = 10
EdgeWeightDict = {}               ## Dictionary For Weight of Edges

EdgeWeightDict[ "similar" ] = 10

EdgeWeightDict[ "is person" ] = 1

EdgeWeightDict[ 'member of band' ] = 2

EdgeWeightDict[ 'tribute' ] = 6

EdgeWeightDict[ 'collaboration ' ] = 4

EdgeWeightDict[ 'vocal supporting musician' ] = 3
EdgeWeightDict[ 'instrumental supporting musician' ] = 3
EdgeWeightDict[ 'supporting musician' ] = 3

EdgeWeightDict[ 'parent' ] = 2
EdgeWeightDict[ 'sibling' ] = 2
EdgeWeightDict[ 'married' ] = 2
EdgeWeightDict[ 'involved with' ] = 3

##----------------------------------------------------------------------------------------


## Funciones ---------------------------------------------------##
def recursiveGraph( G , tempName , depth ):

	## MusicBrainz  Relations -------------------------------------------------------------------------------------------------------------
	relatedList = mz.relatedArtist( G.node[ tempName ][ 'id' ] )
					
	for related_artist in relatedList: 

		if depth >  0 :
			## Si el nodo no esta
			if( not G.has_node( related_artist[0] ) ):
				G.add_node( related_artist[0] , id=related_artist[1] )	
				recursiveGraph( G , related_artist[0] , depth - 1 )

			## Agregar Arista
			G.add_edge( related_artist[0] , tempName , type=related_artist[2] , weight=EdgeWeightDict.get( related_artist[2] , DefaultWeight ) )
		
		else:

			if( G.has_node( related_artist[0] ) ):
				## Agregar Arista
				G.add_edge( related_artist[0] , tempName , type=related_artist[2] , weight=EdgeWeightDict.get( related_artist[2] , DefaultWeight ) )
	## --------------------------------------------------------------------------------------------------------------------------------------
	return 

def graphByArtist( artistName , depth ):

	G = nx.Graph()
	nameId = mz.getArtistId( artistName )
	G.add_node( nameId[0] , id = nameId[1] )
	recursiveGraph( G , nameId[0] , depth )

	return G

def graphByGenre( genre , limit ):

	G = nx.Graph()
	ArtistList = en.getArtistByGenre( genre , limit )

	for artist in ArtistList:
		G.add_node( artist[0] , id = artist[1] )

	## Add Artist Edges
	for artist in ArtistList:

		relatedList = en.relatedArtist( artist[1] )
		
		for related_artist in relatedList:
			## Agregar Arista
			if( not G.has_node( related_artist[0] ) ):
				
				G.add_node( related_artist[0] , id = related_artist[1] )
			
			G.add_edge( related_artist[0] , artist[0] , type=related_artist[2] , weight=EdgeWeightDict.get( related_artist[2] , DefaultWeight ) )
	
	### Fix Loose Ends
	for artist in G.nodes():
		
		relatedList = en.relatedArtist( G.node[ artist ][ 'id' ] )
		
		for related_artist in relatedList:
			## Si el nodo  esta
			if( G.has_node( related_artist[0] ) ):
				## Agregar Arista
				G.add_edge( related_artist[0] , artist , type=related_artist[2] , weight=EdgeWeightDict.get( related_artist[2] , DefaultWeight ) )
	
	return G

## --------------------------------------------------------------##






