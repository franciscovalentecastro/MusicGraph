import matplotlib.pyplot as plt
import operator
import networkx as nx
import closeness as close
import degree as degree
import betweenness as between

### Degree centrality --------------------------------------------
def centrality_degree( G ):
	CentralMeasure = degree.degree_centrality( G )

	return CentralMeasure

### --------------------------------------------------------------

### Closeness centrality --------------------------------------------
def centrality_closeness( G ):
	CentralMeasure = close.closeness_centrality( G )

	return CentralMeasure

### --------------------------------------------------------------

### Betweenness centrality --------------------------------------------
def centrality_betweenness( G ):
	CentralMeasure = between.betweenness_centrality( G )

	return CentralMeasure

### --------------------------------------------------------------

### Eigenvector centrality --------------------------------------------
def centrality_eigenvector( G ):
	CentralMeasure = nx.eigenvector_centrality_numpy( G )

	return CentralMeasure

### --------------------------------------------------------------

### Draw Graph With Centrality Measure --------------------------------------------
def centrality_drawGraph( G , CentralMeasure ):

	color_values = [ CentralMeasure[ node ] for node in G.nodes() ]
	size_values = [ 1000*CentralMeasure[ node ] + 100 for node in G.nodes() ]

	nx.draw_graphviz( G , cmap = plt.get_cmap('Blues') , node_color= color_values , 
			 vmin = 0.0 , vmax = 1.0 , edge_color='b', with_labels = True , node_size = size_values )
	
	##nx.draw( G , """pos=nx.circular_layout(G), """ cmap = plt.get_cmap('YlGn') , node_color=values , 
	##		 vmin = 0.0 , vmax = 1.0 , edge_color='b', with_labels = True , node_size=[v * 10000 for v in d.values()] )

	plt.show()
	
### --------------------------------------------------------------

### Draw Graph With Centrality Measure --------------------------------------------
def centrality_centralNode( G , CentralMeasure , top ):
	sortedList = sorted( CentralMeasure.iteritems(), key=operator.itemgetter(1), reverse=True )[ slice(0,top) ]
	
	print("")
	print("")
	print( "Central Nodes ::::::::::" )
	for node in sortedList:
		print ( node[ 0 ] + " : " + str( node[1] )  )
	
### --------------------------------------------------------------

