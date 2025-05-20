import math

def distance(point_1, point_2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point_1, point_2)))

def mean_cluster(points, clusters, k):
    dim = len(points[0])
    means = []

    for i in range(k):
        cluster_points = [point for idx, point in enumerate(points) if clusters[idx] == i]

        if not cluster_points:
            # Handle empty cluster
            means.append(tuple(0.0 for _ in range(dim)))
            continue

        mean = []
        for d in range(dim):
            dim_sum = sum(point[d] for point in cluster_points)
            mean.append(dim_sum / len(cluster_points))
        means.append(tuple(mean))

    return means

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    centroids = initial_centroids

    for iteration in range(max_iterations):
        clusters = []
        for point in points:
   