
import musicbrainzngs
import sys

musicbrainzngs.set_useragent(
    "python-musicbrainzngs-example",
    "0.1",
    "https://github.com/alastair/python-musicbrainzngs/",
)

def getArtistId( artist_name ):
    result = musicbrainzngs.search_artists( query = artist_name , limit=1 )
    if result['artist-count']  > 0 :
        return ( result['artist-list'][0]['name'] , result['artist-list'][0]['id'] )
    else:
        return (0,0)

def getArtistById( artist_id ):
    try:
        result = musicbrainzngs.get_artist_by_id( artist_id )
    except WebServiceError as exc:
        print("Something went wrong with the request: %s" % exc)
    else:
        if( result ):
            return ( result['artist']['name'] , result['artist']['id'] )
        else:
            return(0,0)


def relatedArtist( artist_id ):
    
    listArtist = []

    try:
        result = musicbrainzngs.get_artist_by_id( artist_id , includes = 'artist-rels' )
    except WebServiceError as exc:
        print("Something went wrong with the request: %s" % exc)
    else:
        
        if "artist-relation-list" in result["artist"]:
            
            for artist in result["artist"]["artist-relation-list"]:
                listArtist.append( ( artist["artist"]["name"] ,  artist["artist"]["id"]  ,  artist["type"] ) )

    return listArtist
