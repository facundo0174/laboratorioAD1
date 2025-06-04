import pandas as pd
from domain.Dataset import DataSet
import requests

class DataSet_API(DataSet):
    def __init__(self, source):
        super().__init__(source)

    def show_api(self):
        pass

    def normalize_api(self):
        pass

    def normalize_list_df(self):
        pass

    def transformar_datos(self):
        #hay que hacer uno nuevo, ya que al ser anidados puede generar errores aplicar strip y quiero conservar los tipos de datos
        pass


    def cargar_datos(self):
        try:
            pass
        except Exception as e:
            print(f"{e}")



"""
df = pd.json_normalize(data, record_path=['provincias', 'municipios'])
print(df)
usas record_path para recuperar 2 o mas diccionarios en datos,
Salida esperada:
id  nombre
0  14001  Córdoba
1  14002  Alta Gracia


Inspecciona siempre la estructura del JSON: Antes de aplicar json_normalize(), utiliza json.dumps()
con una indentación adecuada para visualizar la jerarquía de los datos.

print(json.dumps(data, indent=4))

ejemplo de ver mas de 1 jererquia es decir 2 diccionarios:

data = {
    "provincias": [
        {
            "id": "14",
            "nombre": "Córdoba",
            "municipios": [
                {"id": "14001", "nombre": "Córdoba"},
                {"id": "14002", "nombre": "Alta Gracia"}
            ]
        }
    ]
}

# Aplanar los datos
df = pd.json_normalize(
    data['provincias'],
    record_path=['municipios'],
    meta=['id', 'nombre'],
    meta_prefix='provincia_'
)

print(df)

Salida esperada:

id      nombre       provincia_id provincia_nombre
14001  Córdoba           14          Córdoba
14002  Alta Gracia       14          Córdoba
"""