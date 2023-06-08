import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql import col, row 
from pyspark.sql.functions import udf

# Reference: https://sparkbyexamples.com/pyspark/pyspark-udf-user-defined-function/

spark = SparkSession.builder.appName("Pyspark example").getOrCreate()

columns = ["Seqno","Name"]
data = [("1", "john jones"),
    ("2", "tracey smith"),
    ("3", "amy sanders")]

df = spark.createDataFrame(data=data,schema=columns)

df.show(truncate=False)

#udf
def convertCase(str):
    resStr=""
    arr = str.split(" ")
    for x in arr:
       resStr= resStr + x[0:1].upper() + x[1:len(x)] + " "
    return resStr 

convertDF = df.withColumn("Name", convertCase(col('Name')))

convertDF.show(truncate = False)

#register udf
def upperCase(str):
    return str.upper()

upperCaseUDF = udf(lambda z: upperCase(z), StringType())
# or simply use annotation to skil udf() function
@udf(returnType=StringType()) 
def upperCaseUDF(str):
    return str.upper()

# @udf(returnType=IntegerType())

df.withColumn("Curated Name", upperCaseUDF(col("Name"))).show(truncate=False)

# +-----+-------------+
# |Seqno|Name         |
# +-----+-------------+
# |1    |John Jones   |
# |2    |Tracey Smith |
# |3    |Amy Sanders  |
# +-----+-------------+

# +-----+------------+-------------+
# |Seqno|Name        |Cureated Name|
# +-----+------------+-------------+
# |1    |john jones  |JOHN JONES   |
# |2    |tracey smith|TRACEY SMITH |
# |3    |amy sanders |AMY SANDERS  |
# +-----+------------+-------------+

# register udf and use in sql

spark.udf.register("upperCaseUDF", upperCaseUDF)
df.createOrReplaceTempView("NAME_TABLE")
spark.sql("select Seqno, upperCaseUDF(Name) as CuratedName from NAME_TABLE").show(truncate=False)



# 5.2 Handling null check
# 
# """ null check """

columns = ["Seqno","Name"]
data = [("1", "john jones"),
    ("2", "tracey smith"),
    ("3", "amy sanders"),
    ('4',None)]

df2 = spark.createDataFrame(data=data,schema=columns)
df2.show(truncate=False)
df2.createOrReplaceTempView("NAME_TABLE2")

spark.sql("select convertUDF(Name) from NAME_TABLE2") \
     .show(truncate=False)
# will get error 
# AttributeError: 'NoneType' object has no attribute 'split'

# correct way
spark.udf.register("_nullsafeUDF", lambda str: convertCase(str) if not str is None else "" , StringType())

spark.sql("select _nullsafeUDF(Name) from NAME_TABLE2") \
     .show(truncate=False)

spark.sql("select Seqno, _nullsafeUDF(Name) as Name from NAME_TABLE2 " + \
          " where Name is not null and _nullsafeUDF(Name) like '%John%'") \
     .show(truncate=False)    
