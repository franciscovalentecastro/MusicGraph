import heapq
import networkx as nx
import random

# Funciones auxiliares para betweenness

def shortest_path_BFS(G,s):
    S=[] 
    P={} #predecesores
    for v in G:
        P[v]=[]
    sigma=dict.fromkeys(G,0.0) # sigma[v]=0 para cada v en G, donde sigma son las distancias
    D={} #"colores"
    sigma[s]=1.0
    D[s]=0
    Q=[s] #Cola
    while Q:   # Usar BFS para encontrar el camino más corto
        v=Q.pop(0)
        S.append(v) #Agregar al final
        Dv=D[v]
        sigmav=sigma[v]
        for w in G[v]:
            if w not in D:
                Q.append(w)
                D[w]=Dv+1
            if D[w]==Dv+1: # Este es el camino más corto, cuenta los caminos
                sigma[w] += sigmav
                P[w].append(v) # Predecesores
    return S,P,sigma


def dijkstra(G,s,weight='weight'):
    S=[]
    P={}
    for v in G:
        P[v]=[]
    sigma=dict.fromkeys(G,0.0)# sigma[v]=0 para cada v en G 
    D ={}
    sigma[s]=1.0
    push=heapq.heappus 
    pop=heapq.heappop
    seen = {s:0}
    Q=[]   # Q es un montículo con tuplas (distance,node id).
    push(Q,(0,s,s))
    while Q:
        (dist,pred,v)=pop(Q)
        if v in D:
            continue # Ya buscó este nodo
        sigma[v] += sigma[pred] # Cuenta los caminos
        S.append(v)
        D[v] = dist
        for w,edgedata in G[v].items():
            vw_dist = dist + edgedata.get(weight,1)
            if w not in D and (w not in seen or vw_dist < seen[w]):
                seen[w] = vw_dist
                push(Q,(vw_dist,v,w))
                sigma[w]=0.0
                P[w]=[v]
            elif vw_dist==seen[w]:  # manipular los mismo caminos
                sigma[w] += sigma[v]
                P[w].append(v)
    return S,P,sigma

def accumulate(betweenness,S,P,sigma,s):
    delta=dict.fromkeys(S,0)
    while S:
        w=S.pop()
        coeff=(1.0+delta[w])/sigma[w]
        for v in P[w]:
            delta[v] += sigma[v]*coeff
        if w != s:
            betweenness[w]+=delta[w]
    return betweenness

def accumulate_endpoints(betweenness,S,P,sigma,s):
    betweenness[s]+=len(S)-1
    delta=dict.fromkeys(S,0)
    while S:
        w=S.pop()
        coeff=(1.0+delta[w])/sigma[w]
        for v in P[w]:
            delta[v] += sigma[v]*coeff
        if w != s:
            betweenness[w] += delta[w]+1
    return betweenness

def rescale(betweenness,n,normalized,directed=False,k=None):
    if normalized is True:
        if n <=2:
            scale=None  # no normalizar b=0 para todos los nodos
        else:
            scale=1.0/((n-1)*(n-2))
    else: # rescalar por 2 para grafos no dirigidos
        if not directed:
            scale=1.0/2.0
        else:
            scale=None
    if scale is not None:
        if k is not None:
            scale=scale*n/k
        for v in betweenness:
            betweenness[v] *= scale
    return betweenness


#Algoritmo Betweenness 
def betweenness_centrality(G): #G es un grafo de networkX

    normalized=True
    weight=None
    endpoints=False
    
    betweenness=dict.fromkeys(G,0.0) # b[v]=0 for v in G. Crea en diccionario, asignando el valor 0 a cada vértice.
    nodes = G

    for s in nodes:
        # Caminos más cortos
        if weight is None:  # usar BFS
            S,P,sigma=shortest_path_BFS(G,s)
        else:  # Usar algoritmo Dijkstra
            S,P,sigma=dijkstra(G,s,weight)
        # Acumulación
        if endpoints:
            betweenness=accumulate_endpoints(betweenness,S,P,sigma,s)
        else:
            betweenness=accumulate(betweenness,S,P,sigma,s)
    # Rescalar
    betweenness=rescale(betweenness, len(G),normalized=normalized,directed=G.is_directed(),k=k)

    return betweenness
