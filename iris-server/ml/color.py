import numpy as np
from sklearn.cluster import KMeans
from PIL import Image


def analyze_colors(image_path, n_clusters=5):
    image = Image.open(image_path)
    # Cheat a bit and resize the image
    image = image.resize((200, 200), Image.ANTIALIAS)
    # Convert to list of RGB triplets
    reshaped_image = np.array(image).reshape((image.size[0] * image.size[1], 3))
    kmeans = KMeans(n_clusters=n_clusters, n_jobs=4)
    kmeans.fit(reshaped_image)
    centroids = kmeans.cluster_centers_
    hist = np.histogram(kmeans.labels_, n_clusters)[0]
    hist_dict = dict(zip(np.arange(0, n_clusters + 1), hist))
    sorted_hist_dict = sorted(hist_dict.items(), key=lambda x: x[1],
                              reverse=True)
    sorted_centroids = [centroids[pos] for pos, key in sorted_hist_dict]
    colors = []
    for cen in sorted_centroids:
        rgb = []
        for col in cen:
            rgb.append(int(col))
        colors.append(rgb)
    return colors
