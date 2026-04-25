# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS sdp_catalog.source.products
# MAGIC (
# MAGIC   product_id INT,
# MAGIC   product_name STRING,
# MAGIC   category STRING,
# MAGIC   subcategory STRING,
# MAGIC   updated_at TIMESTAMP
# MAGIC );
# MAGIC
# MAGIC INSERT INTO sdp_catalog.source.products
# MAGIC VALUES
# MAGIC   (1, 'Product1', 'Category1', 'Subcategory1', current_timestamp()),
# MAGIC   (2, 'Product2', 'Category2', 'Subcategory2', current_timestamp()),
# MAGIC   (3, 'Product3', 'Category3', 'Subcategory3', current_timestamp()),
# MAGIC   (4, 'Product4', 'Category4', 'Subcategory4', current_timestamp()),
# MAGIC   (5, 'Product5', 'Category5', 'Subcategory5', current_timestamp());

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM sdp_catalog.source.products;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM sdp_catalog.target.products_scd2;

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO sdp_catalog.source.products
# MAGIC VALUES
# MAGIC   (3, 'Product3', 'Category5', 'Subcategory7', current_timestamp());

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM sdp_catalog.target.products_scd1;