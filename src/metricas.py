min_cluster_range = 2
max_cluster_range = 20

def optimal_number_of_clusters(wcss, min_cluster_range, max_cluster_range):
    """
    Calcula a maior distância entre os pontos que marcam as 
    somas dos quadrados intra-clusters para 19 calculadas 
    com `calculate_wcss()`
    
    Parametros
    ----------
    wcss : lista
        lista contendo os valores de soma de quadrados intra-cluster
    min_cluster_range : int
        numero minimo de clusters
    max_cluster_range : int
        numero maximo de clusters
    
    Returns
    -------
    int : número de clusters 
    """
    from math import sqrt
    x1, y1 = min_cluster_range, wcss[0]
    x2, y2 = max_cluster_range, wcss[len(wcss)-1]

    distances = []
    for i in range(len(wcss)):
        x0 = i+2
        y0 = wcss[i]

        numerator = abs((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1)
        denominator = sqrt((y2 - y1)**2 + (x2 - x1)**2)
        distances.append(numerator/denominator)
    return distances.index(max(distances)) + 2


def calculate_wcss(data, min_cluster_range, max_cluster_range):
    """
    Calcula a soma dos quadrados intra-clusters para 19
    quantidades de clusters, iniciando com o mínimo de 2 clusters
    
    Parametros
    ----------
    data : DataFrame
        conjunto de dados para fazer o `.fit()` do KMeans
    min_cluster_range : int
        numero minimo de clusters
    max_cluster_range : int
        numero maximo de clusters

    
    Returns
    -------
    wcss : lista contendo os valores de soma de quadrados intra-cluster
    """
    from sklearn.cluster import KMeans
    wcss = []
    for n in range(min_cluster_range, max_cluster_range):
        kmeans = KMeans(n_clusters=n)
        kmeans.fit(X=data)
        wcss.append(kmeans.inertia_)

    return wcss
