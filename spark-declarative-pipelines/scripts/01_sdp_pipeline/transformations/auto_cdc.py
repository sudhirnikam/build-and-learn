from pyspark import pipelines as dp
from pyspark.sql.functions import *

#Empty streaming table for type2 
dp.create_streaming_table(name="products_scd2")

#Empty streaming table for type1
dp.create_streaming_table(name="products_scd1")

# Streaming view
@dp.temporary_view
def products_source():
    df = spark.readStream.table("sdp_catalog.source.products")
    return df


# SCT Type-2
dp.create_auto_cdc_flow(
  target = "products_scd2",
  source = "products_source",
  keys = ["product_id"],
  sequence_by = col("updated_at"),
  except_column_list = ["updated_at"],
  stored_as_scd_type = "2"
)


# SCT Type-1
dp.create_auto_cdc_flow(
  target = "products_scd1",
  source = "products_source",
  keys = ["product_id"],
  sequence_by = col("updated_at"),
  except_column_list = ["updated_at"],
  stored_as_scd_type = "1"
)

