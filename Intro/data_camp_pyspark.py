# Data camp pyspark

from pyspark.sql import SparkSession
print(sc) #SparkContext
print(sc.version) 

# Import SparkSession from pyspark.sql

# Create my_spark
my_spark = SparkSession.builder.getOrCreate() # Is a singleton whihch returns a session if exists else creates one.
# Print my_spark
print(my_spark)


# Print the tables in the catalog
print(spark.catalog.listTables())

# Don't change this query
query = "FROM flights SELECT * LIMIT 10"

# Get the first 10 rows of flights
flights10 = spark.sql(query)

# Show the results
flights10.show()

# Don't change this query
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"

# Run the query
flight_counts = spark.sql(query)

# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas() # Create a pandas data frame for spark context.

# Print the head of pd_counts
print(pd_counts.head())

## Create temp tables in spark session from pandas dataframe.
# Create pd_temp
pd_temp = pd.DataFrame(np.random.random(10))

# Create spark_temp from pd_temp 
# data cannot be used in other context we have to persist to cluster or temporary table.
spark_temp = spark.createDataFrame(pd_temp)

# Examine the tables in the catalog
print(spark.catalog.listTables())

# Add spark_temp to the catalog
spark_temp.createOrReplaceTempView('temp')

# Examine the tables in the catalog again
print(spark.catalog.listTables())


### Load data directly into spark cluster.

# Don't change this file path
file_path = "/usr/local/share/datasets/airports.csv"

# Read in the airports data
airports = spark.read.csv(file_path, header=True)

# Show the data
airports.show()
