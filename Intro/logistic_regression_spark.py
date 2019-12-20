from pyspark.ml import pipeline
from pyspark.ml.classification import LogisticRegression

train = spark.read.format('csv').options(header='true', inferSchema='true').load()
