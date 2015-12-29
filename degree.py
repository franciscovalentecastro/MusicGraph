import networkx as nx

def degree_centrality(G):
    
	degree = {}
	s = 1.0/(len(G)-1.0)
	degree = dict((n,d*s) for n,d in G.degree_iter()) #Guarda en el diccionario.
	#degree_inter: Regresa un iterador para (node, degree).

	return degree


