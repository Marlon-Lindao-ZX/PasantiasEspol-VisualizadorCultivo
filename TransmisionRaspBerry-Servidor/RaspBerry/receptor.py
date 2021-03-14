from time import sleep, time, time_ns
import pandas as pd

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

tiempo=5

# You can generate a Token from the "Tokens Tab" in the UI
token = "ykfqgonxlAdQQO1XBoNJWkyC4xM3f0N8JHZg3_ezo1NVTYX4cE3US1TpY_-xuXXfPwd2vO9oQpAqa5PiMCk9uA=="
org = "ESPOL"
bucket = "Prueba 3"

client = InfluxDBClient(url="http://192.168.100.11:8086", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)

df = pd.read_csv("data.csv",sep=';')

for d in range(len(df)):
    print("Activo, leyendo linea #"+str((d+1))+"...")
    name = str(df["nombre"][d]).replace(" ", "")
    linea = "central" + ",sensor="+ name + " " + "temperatura=" + str(df["temperatura"][d]) + "," + "humedad=" + str(df["humedad"][d]) + "," + "ph=" + str(df["ph"][d]) + "," + "precipitacion=" + str(df["precipitacion"][d]) + " " + str(time_ns())
    print(linea)
    write_api.write(bucket, org, linea)
    print("A dormir por" + str(tiempo) + " segundos")
    sleep(tiempo)


'''
lines = ["price"
         + ",type=BTC"
         + " "
         + "close=" + str(df["close"][d]) + ","
         + "high=" + str(df["high"][d]) + ","
         + "low=" + str(df["low"][d]) + ","
         + "open=" + str(df["open"][d]) + ","
         + "volume=" + str(df["volume"][d])
         + " " + str(time_ns()) for d in range(len(df))]

write_api.write(bucket, org, lines)
'''