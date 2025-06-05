import pandas as pd
from domain.Dataset import DataSet
import requests
import json

class DataSet_API(DataSet):
    def __init__(self, source):
        super().__init__(source)

    def show_api(self,dfjson):
        print(json.dumps(dfjson, indent=4, ensure_ascii=False))
        #mostramos la forma de la api para observar y razonar como aplanar los datos

    def dataNormalize(self, df, record_path=None, meta=None, meta_prefix=None, sep='_'):
        """
        encapsulamos el metodo normalize de pandas para manipularlo segun sea necesario debido
        a la estructura cambiante de la api, la cual se debe razonar tabulizar correctamente
        """
        return pd.json_normalize(df,record_path=record_path,meta=meta,meta_prefix=meta_prefix,sep=sep)

    def stringNormalizer(self,json):
        """
        el stack guarda los elementos a analizar, donde el 
        padre de la estuctura es el contenido del primer none, y el segundo sera la clave o indice
        mientras que el 3cero sera el contenido
        basicamente  se utiliza una pila de 3 elementos basicos, nomVarible, Posicion y valor para modificar y
        normalizar los strings
        el primer stack es la totalidad de anidamientos de la api, hasta que no se procese toda la informacion
        no terminara
        """
        stack = [(None, None, json)]  
        while stack:
            padre, clave, valor = stack.pop()
            if isinstance(valor, dict):
                for k, v in valor.items():
                    stack.append((valor, k, v))
            elif isinstance(valor, list):
                for i, item in enumerate(valor):
                    stack.append((valor, i, item))
            elif isinstance(valor, str):
                normalizado = valor.strip().lower()
                if isinstance(padre, dict):
                    padre[clave] = normalizado
                elif isinstance(padre, list):
                    padre[clave] = normalizado
        return json

    def transformar_datos(self):
        self.data=self.data.drop_duplicates()
    #https://apis.datos.gob.ar/georef/api/provincias
    def cargar_datos(self):
        try:
            response=requests.get(self.source)
            if response.status_code==200:
                self.show_api(df)##muestra  la api para razonar el aplanamiento de datos
                df=response.json()
                df=self.stringNormalizer(df)
                df=self.dataNormalize(df,"provincias")
                self.data=df
                if self.validar_datos():
                    self.transformar_datos()
                    print("carga exitosa de api")
            else:
                print("error de respuesta en la api")
        except Exception as e:
            print(f"error de carga de api{e}")
