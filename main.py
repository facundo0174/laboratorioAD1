from domain.Dataset_api import DataSet_API
from domain.Dataset_csv import DataSetCSV
from domain.Dataset_exel import DataSetEXEL
from os import path
from data.Data_saver import DataSaver

api_path="https://apis.datos.gob.ar/georef/api/provincias"
exel_path=path.join(path.dirname(__file__),"files/srg_pimes_asistidas.xlsx")
csv_path=path.join(path.dirname(__file__),"files/comercio-interno.csv")

obj_exel=DataSetEXEL(exel_path)
obj_csv=DataSetCSV(csv_path)
obj_api=DataSet_API(api_path)

obj_exel.dataCharge()
obj_api.dataCharge()
obj_csv.dataCharge()

""" si hiciera falta observamos, en el caso de api obligadamente lo hacemos para normalizar correctamente
    ya que se debe modificar el dataset api segun las claves posibles que tenga y posibles meta datos

    obj_csv.dfInspect()
"""
db=DataSaver()
db.saveDataFrame(obj_api.data,"provincias_api")
db.saveDataFrame(obj_csv.data,"comercio_interno")
db.saveDataFrame(obj_exel.data,"srg_pimes_asistidas")

csv_path=path.join(path.dirname(__file__),"files/medicamentos.csv")
obj_csv=DataSetCSV(csv_path)
obj_csv.dataCharge()
db.saveDataFrame(obj_csv.data,"medicamentos")

exel_path=path.join(path.dirname(__file__),"files/srg_vigentes_acreedor.xlsx")
obj_exel=DataSetEXEL(exel_path)
obj_exel.dataCharge()
db.saveDataFrame(obj_exel.data,"srg_vigentes_acreedores")




