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
        errors=[]
        if self.data.empty:
            errors.append("el dataframe esta vacio (empty)")
        if self.data is None:
            errors.append("el dataframe esta vacio (none)")
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
        

    
    def transformar_datos(self):#solo para archivos planos es decir cualquier cosa menos API's
        if self.data is not None:
            self.data.columns = self.data.column.str.lower().str.replace(" ","_")
            self.data = self.data.drop_duplicates()
            # para asegurar el tipo de dato de las columnas y evitar errores de metodos de objetos NO strings
            #ademas asi conservamos el tipo de datos de otras cosas que no sean strings
            for col in self.data.select_dtypes(include="object").columns:
                if isinstance(self.data[col].iloc[0], str): 
                    self.data[col] = self.data[col].astype(str).str.strip()
                else:
                    self.data[col] = self.data[col]            


    def dataInfo(self):
        print(self.data.describe())

    
