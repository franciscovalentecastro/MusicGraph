# -*- encoding: utf-8 -*-
import networkx as nx

def closeness_centrality(G):

	normalized=True
	distance=None
	v = None
	
	if distance is not None:
        	if distance is True: distance='weight'
        		path_length=functools.partial(nx.single_source_dijkstra_path_length,
                                      weight=distance)
	#Calcula la longitud del camino más corto entre la fuente y todos los demás nodos alcanzables para un grafo con pesos
    	else:
        	path_length=nx.single_source_shortest_path_length

    	if v is None:
       		nodes=G.nodes()
    	else:
        	nodes=[v]
    	closeness={}

	for n in nodes:
		sp = path_length(G,n) #Calcular las longitudes de los caminos más cortos
		total_sp=sum(sp.values()) #Sumar los valores de las longitudes
		if total_sp > 0.0 and len(G) > 1:
		    closeness[n]= (len(sp)-1.0) / (total_sp)
		    # normalize to number of nodes-1 in connected part
		    if normalized:
			s=(len(sp)-1.0) / ( len(G) - 1 )
			closeness[n] *= s
		else:                                                                
		    closeness[n]=0.0          

	return closeness





