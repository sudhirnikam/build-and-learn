from pyspark import pipelines as dp
from pyspark.sql.functions import *

#Streaming View
@dp.temporary_view(name="src_sales_view")
def src_sales_stream():
    df = spark.readStream.table("sdp_catalog.source.sales")
    df = df.withColumn("date", to_date(col("date"), "MM-dd-yyyy"))
    return df

#Streaming Table
@dp.table(name = "enr_sales_view_stream")
def enr_sales():
    df = spark.readStream.table("src_sales_view")
    df = df.withColumn("revenue", col("revenue") * 1.05)
    return df

#Streaming Table
@dp.table(name = "cur_sales_view_stream")
def cur_sales():
    df = spark.readStream.table("enr_sales_view_stream")
    df = df.groupBy("date").agg(sum("revenue").alias("total_revenue"))
    return df
