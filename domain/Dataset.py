from abc import ABC, abstractmethod
from pathlib import Path
import pandas as pd
import json

class DataSet(ABC):
    def __init__(self,source):
        self.__data=None
        self.__source=source
    @property
    def data(self):
        #getter y procesar
        return(self.__data)
    @property
    def source(self):
        return (self.__source) 
    @data.setter
    def data(self, df):
        #validaciones de si datasetter es correcto segun x cosa
        if isinstance (df, pd.DataFrame):
            self.__data=df
        else:
            raise(ValueError("error, tipo esperado pandas en data frame"))
    @abstractmethod
    def dataCharge(self):# carga de datos unico para cada tipo de dato
        pass
    @abstractmethod
    def dfInspect(self):#inspector del dataframe unico para cada tipo de archivo
        pass
    
    def extDevolution(self):#retorno de extencion del archivo
        if (Path(self.source).suffix == ""):
            raise ValueError("error el archivo no tiene extencion")
        else:
            return (Path(self.source).suffix)
    def dataValidation(self):# validaciones de formato no aceptables
        errors=[]
        if self.data is None:
            errors.append("el dataframe esta vacio (none)")
        if self.data.empty:
            errors.append("el dataframe esta vacio (empty)")
        if self.data.isnull().sum().sum()>0:
            errors.append("el dataframe posee valores nulos en su interior")
        if self.data.duplicated().sum()>0:
            errors.append("el dataframe posee valores duplicados en su interior")
        
        if errors:
            print("Las validaciones detectaron las siguientes cirscunstancias:\n")
            for e in errors:
                print(f"#{e}\n")
            return False
        else:
            return True
    def dataTransformation(self):#solo para archivos planos es decir cualquier cosa menos API's
        if self.data is not None:
            self.data.columns = self.data.columns.str.lower().str.replace(" ","_")#modificamos nombres de las columnas
            self.data = self.data.drop_duplicates()# eliminamos filas duplicadas realizando comparaciones entre filas/registros
            # para asegurar el tipo de dato del contenidodde las columnas y evitar errores de metodos de objetos NO strings
            #ademas asi conservamos el tipo de datos de otras cosas que no sean strings
            
            for col in self.data.select_dtypes(include="object").columns:
                self.data[col] = self.data[col].apply(lambda x: x.strip() if isinstance(x, str) else x)
    def dataInfo(self):#informacion estadistica basica del dataframe
        print(self.data.describe())
    def dfShowInfo(self,df):#informacion redundante del dataframe
        if self.extDevolution()!= ".json":
            print("primeros 5 elementos:")
            print(df.head())
            print("___###___")
            print("ultimos 5 elementos:")
            print(df.tail())
            print("___###___")
            print("nombres de columnas")
            print(df.columns)
            print("___###___")
            print("tipos de datos de columnas")
            print(df.dtypes)
            print("___###___")
            print("duplicados")
            print(df.duplicated())
            print("___###___")
            print("total de duplicados")
            print(df.duplicated().sum())
            print("___###___")
            print("cantidad de nulos")
            print(df.isnull().sum())
            print("___###___")
            print("informacion de indice, columnas tipos...")
            print(df.info())
            print("___###___")
            print("tamaño total de elementos filas x tablas")
            print(df.size)
            print("___###___")
            print("dimencion")
            print(df.shape)
            print("___###___")
        else:
            print(json.dumps(df, indent=4, ensure_ascii=False))