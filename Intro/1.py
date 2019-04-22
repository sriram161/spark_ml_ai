"""
 Spark dataframes
"""
emp_df = spark.read.csv("sample.csv")
emp_df

emp_df.schema

emp_df.printSchema()

emp_df.columns

emp_df.take(5)

emp_df.count()

sample_df = emp_df.sample(False, 0.1) # sampling without replacemment.
sample_df.count()

emp_managers_df = emp_df.filter("salary" >= 100000)
emp_manageres_df.count()

emp_managerers_df.select("salary").show()