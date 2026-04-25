# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE sdp_catalog.source.sales(
# MAGIC   order_id INT,
# MAGIC   product_id INT,
# MAGIC   revenue FLOAT,
# MAGIC   date DATE,
# MAGIC   store_id INT
# MAGIC );
# MAGIC
# MAGIC INSERT INTO sdp_catalog.source.sales VALUES
# MAGIC (1, 100, 100.00, '2022-01-01', 1),
# MAGIC (2, 101, 200.00, '2022-01-02', 1),
# MAGIC (3, 102, 300.00, '2022-01-03', 1),
# MAGIC (4, 103, 400.00, '2022-01-04', 1),
# MAGIC (5, 104, 500.00, '2022-01-05', 1);

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sdp_catalog.source.sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO sdp_catalog.source.sales VALUES
# MAGIC (6, 104, 500.00, '2022-01-06', 1),
# MAGIC (7, 104, 500.00, '2022-01-07', 1);

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO sdp_catalog.source.sales VALUES
# MAGIC (8, 101, 400.00, '2022-01-04', 2),
# MAGIC (9, 102, 300.00, '2022-01-05', 2);

# COMMAND ----------

# MAGIC %sql
# MAGIC select distinct date from sdp_catalog.source.sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO sdp_catalog.source.sales VALUES
# MAGIC (10, 101, 200.00, '2022-01-06', 2),
# MAGIC (11, 102, 700.00, '2022-01-07', 2);

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO sdp_catalog.source.sales VALUES
# MAGIC (12, 101, 200.00, '2022-01-06', 2),
# MAGIC (13, 102, 700.00, '2022-01-07', 2);