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
    response = en.get('genre/artists', name=genre , results = limit )
    listArtist = []
    
    for artist in response['artists']: 
    	listArtist.append( ( artist["name"] , artist["id"]  ) )

    return listArtist

def relatedArtist( artist_id ):
    
    listArtist = []

    ##try:
    bk = artist.Artist( artist_id )
    ##except WebServiceError as exc:
    ##    print("Something went wrong with the request: %s" % exc)
    ##else:

    similar = artist.similar( ids = bk.id , results = 5 )
        
    for similar_artist in similar:            
        listArtist.append( ( similar_artist.name ,  similar_artist.id  ,  "similar" ) )

    return listArtist

## --------------------------------------------------------------##





