# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS sdp_catalog.source.sales_north(
# MAGIC   order_id INT,
# MAGIC   product_id INT,
# MAGIC   revenue FLOAT,
# MAGIC   date DATE,
# MAGIC   store_id INT,
# MAGIC   region STRING
# MAGIC );
# MAGIC
# MAGIC INSERT INTO sdp_catalog.source.sales_north VALUES
# MAGIC (1, 100, 100.00, '2022-01-01', 1, 'North'),
# MAGIC (2, 101, 200.00, '2022-01-02', 1, 'North'),
# MAGIC (3, 102, 300.00, '2022-01-03', 1, 'North'),
# MAGIC (4, 103, 400.00, '2022-01-04', 1, 'North'),
# MAGIC (5, 104, 500.00, '2022-01-05', 1, 'North');

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO sdp_catalog.source.sales_north VALUES
# MAGIC (6, 100, 100.00, '2022-01-01', 1, 'North'),
# MAGIC (7, 101, 200.00, '2022-01-02', 1, 'North');

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sdp_catalog.source.sales_north;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS sdp_catalog.source.sales_south(
# MAGIC   order_id INT,
# MAGIC   product_id INT,
# MAGIC   revenue FLOAT,
# MAGIC   date DATE,
# MAGIC   store_id INT,
# MAGIC   region STRING
# MAGIC );
# MAGIC
# MAGIC INSERT INTO sdp_catalog.source.sales_south VALUES
# MAGIC (1, 100, 100.00, '2022-01-01', 1, 'South'),
# MAGIC (2, 101, 200.00, '2022-01-02', 1, 'South'),
# MAGIC (3, 102, 300.00, '2022-01-03', 1, 'South'),
# MAGIC (4, 103, 400.00, '2022-01-04', 1, 'South'),
# MAGIC (5, 104, 500.00, '2022-01-05', 1, 'South');

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sdp_catalog.source.sales_south;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sdp_catalog.target.total_sales;