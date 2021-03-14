from datetime import datetime
from time import time, time_ns
import pandas as pd

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "ykfqgonxlAdQQO1XBoNJWkyC4xM3f0N8JHZg3_ezo1NVTYX4cE3US1TpY_-xuXXfPwd2vO9oQpAqa5PiMCk9uA=="
org = "ESPOL"
bucket = "Prueba2"

client = InfluxDBClient(url="http://localhost:8086", token=token)

query = f'from(bucket: \"{bucket}\") |> range(start: -1h)'
print(query)
tables = client.query_api().query(query, org=org)

print(query)

#print(time_ns())