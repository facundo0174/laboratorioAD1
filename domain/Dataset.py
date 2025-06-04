from abc import ABC, abstractmethod

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
    def data(self, value):
        #validaciones de si datasetter es correcto segun x cosa
        self.__data=value
    @abstractmethod
    def cargar_datos(self):
        pass
    
    def validar_datos(self):
        pass
    
    def transformar_datos(self):#solo para archivos planos es decir cualquier cosa menos API's
        if self.data is not None:
            self.__data.columns = self.data.column.str.lower().str.replace(" ","_")
            self.__data = self.data.drop_duplicates()
            for col in self.data.select_dtypes(include="object").columns:
                if isinstance(self.data[col].iloc[0], str): # para asegurar el tipo de dato de las columnas y evitar errores de metodos de objetos NO strings
                    self.data[col] = self.data[col].astype(str).str.strip()
                else:
                    self.data[col] = self.data[col]            


    def informar_datos(self):
        pass

    
