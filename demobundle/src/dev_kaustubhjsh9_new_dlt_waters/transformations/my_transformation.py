from pyspark import pipelines as dp

from pyspark_datasources import OpenSkyDataSource
spark.dataSource.register(OpenSkyDataSource)
@dp.table(
  name="ingest_flights",
  comment="Streaming table ingesting data from opensky format"
)

def ingest_flights():
  return (
    spark.readStream
      .format("opensky")
      .load()
  )
