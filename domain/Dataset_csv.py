from domain.Dataset import DataSet
import pandas as pd
import chardet

class DataSetCSV(DataSet):

    def __init__(self, source):
        super().__init__(source)

    def dataCharge(self):
        try:
            if self.extDevolution(self.source)==".csv":#comprobamos que solo se pueda utilizar con .csv
                df=pd.read_csv(self.source)
                self.data=df
                if self.dataValidation():
                    self.dataTransformation()
                    print("csv cargado exitosamente")
            else:
                raise(ValueError("error, el archivo no es un .csv"))
        except Exception as e:
            print(f"error de carga csv{e}")
    
    def dfInspect(self):#inicializamos temporalmente un df para muestreo 
        try:
            if self.extDevolution()==".csv":#comprobamos que solo se pueda utilizar con .csv
                df=pd.read_csv(self.source, encoding=self.getCodification())
                self.dfShowInfo(df)
        except Exception as e:
            print(f"error al inspeccionar el dataframe, {e}")

    def getCodification(self):#existen diferentes codificaciones csv
        with open(self.source,"rb") as file:
            d=file.read(10000)#limitamos la cantidad de lectura a 10kbytes
            r=chardet.detect(d)
            return r['encoding']

