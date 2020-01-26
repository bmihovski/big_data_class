import numpy as np
from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans, KMeansModel

sc = SparkContext("local", "My Simple App")

data = sc.textFile("train.csv")

# skip header
data = data.filter(lambda line: line[0] != "l")
data = data.filter(lambda line: line[0] != 'l')

parsed = data.map(lambda line: np.array([float(x) for x in line.split(",")[1:]]))

clusters = KMeans.train(parsed, 10, maxIterations=10, runs=1, initializationMode="random")


def error(pt):
    center = clusters.centers[clusters.predict(pt)]
    return np.sqrt(sum([x ** 2 for x in (pt - center)]))


wssse = parsed.map(lambda pt: error(pt)).reduce(lambda x, y: x + y)
print(f"Within set sum of squared error: {wssse}")

