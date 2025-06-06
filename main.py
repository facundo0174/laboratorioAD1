from domain.Dataset_api import DataSet_API
from domain.Dataset_csv import DataSetCSV
from domain.Dataset_exel import DataSetEXEL
from os import path
from data.Data_saver import DataSaver

api_path="https://apis.datos.gob.ar/georef/api/provincias"
exel_path=path.join(path.dirname(__file__),"files/")
csv_path=path.join(path.dirname(__file__),"files/comercio-interno.csv")
#https://infra.datos.gob.ar/georef/localidades_censales.json

#obj_exel=DataSetEXEL(exel_path)
obj_csv=DataSetCSV(csv_path)
#obj_api=DataSet_API(api_path)

obj_csv.dfInspect()
