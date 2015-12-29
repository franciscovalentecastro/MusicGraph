import networkx as nx
from networkx_viewer import Viewer
import sys
import json
from networkx.readwrite import json_graph

## Get Save Name
fileName = sys.argv[1]

## load json formatted data
json_data=open( fileName )
data = json.load( json_data )

## Create Graph from data
G = json_graph.node_link_graph( data )

app = Viewer(G)
app.mainloop()