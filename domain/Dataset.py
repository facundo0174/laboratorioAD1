from abc import ABC, abstractmethod
from pathlib import Path
import pandas as pd

class DataSet(ABC):
    def __init__(self,data,source):
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
    def dataCharger(self):
        pass
    
    def extDevolution(self):
        return (Path(self.source).suffix)

    def dataValidation(self):
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
            print("Los errores encontrados son los siguientes:\n")
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

    def dataInfo(self):
        print(self.data.describe())

    
