data = [
    [1, 2], [2, 3], [2, 1],
    [8, 8], [9, 10], [10, 8]
]
centroids = [[1, 2], [8, 8]]
while True:
    clusters = [[], []]
    for point in data:
        distances = []

        for center in centroids:
            distance = ((point[0] - center[0]) ** 2 +
                        (point[1] - center[1]) ** 2) ** 0.5

            distances.append(distance)

        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)

    new_centroids = []

    for cluster in clusters:
        x = sum(point[0] for point in cluster) / len(cluster)
        y = sum(point[1] for point in cluster) / len(cluster)

        new_centroids.append([x, y])

    if new_centroids == centroids:
        break

    centroids = new_centroids

for i in range(len(clusters)):
    print("Cluster", i + 1, ":", clusters[i])
    print("Centroid:", centroids[i])
