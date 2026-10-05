# Spark Session to read and print employees_records.csv
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("EmployeeRecordsSession") \
    .getOrCreate()

# sc = spark.sparkContext

orders = spark.read.csv("orders_dataset.csv", header=True, inferSchema=True)
customers = spark.read.csv("customers_dataset.csv", header=True, inferSchema=True)
products = spark.read.csv("products_dataset.csv", header=True, inferSchema=True)
orders.show(10)
# Create 3 temporary tables/views
orders.createOrReplaceTempView("orders")
customers.createOrReplaceTempView("customers")
products.createOrReplaceTempView("products")