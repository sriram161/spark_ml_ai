"""
 Spark mllib

Algorithms ->
Classification
regression
clustering
topic modelling.
etc.

workflows ->
feature transformations
pipelines
evaluations 
hyperparameter
tuning

utilities ->
Distributed math libraries
statistics
functions
"""

# Normalize -> maps data from original range to range of 0 to 1
# Advantage of Normalization is large range values and small range values are brough to common range and that is 0 to 1.

# Standardize -> Maps data from origninal range to range -1 to 1 
# mean is 0
# normally distributed with standard deviation of 1
# Used when features have different scales and 
# ML algorithms assume a normal distribution.

# Patitioning -> Maps data value from continuous values to buckets
# Deciles and percentiles ane examples of buckets
# useful when you want to work with groups of values 
# instead of a continuous range of values.

# TEXT: TOkeniziong -> list of words.
# TEXT: TF-IDF -> Maps text from a single, typically long strings to a vector of frequencies of each word relative to a text.
# TF-IDF assumes infrequently used workds are more useful to classify text.

##### NORMALIZING
