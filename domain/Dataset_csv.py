from domain.Dataset import DataSet
import pandas as pd
import chardet
import csv

class DataSetCSV(DataSet):

    def __init__(self, source):
        super().__init__(source)

    def dataCharge(self):
        try:
            if self.extDevolution()==".csv":#comprobamos que solo se pueda utilizar con .csv
                df=pd.read_csv(self.source, encoding=self.getCodification(), sep=self.getSeparator(), errors="replace")
                self.data=df
                if self.dataValidation():
                    self.dataTransformation()
                    print("csv cargado exitosamente")
                else:
                    print("csv cargado con cirscunstancias")
            else:
                raise(ValueError("error, el archivo no es un .csv"))
        except Exception as e:
            print(f"error de carga csv {e}")
    
    def dfInspect(self):#inicializamos temporalmente un df para muestreo 
        try:
            if self.extDevolution()==".csv":#comprobamos que solo se pueda utilizar con .csv
                df=pd.read_csv(self.source, encoding=self.getCodification(), sep=self.getSeparator(), errors="replace")
                self.dfShowInfo(df)
        except Exception as e:
            print(f"error al inspeccionar el dataframe, {e}")

    def getCodification(self):#existen diferentes codificaciones binarias de csv
        with open(self.source,"rb") as file:
            d=file.read(50000)#limitamos la cantidad de lectura a 50kbytes
            r=chardet.detect(d)
            return r['encoding']
    
    def getSeparator(self):# existen diferentes separadores de datos
        with open(self.source, 'r') as file:
            dialect = csv.Sniffer().sniff(file.read(1024))
            s = dialect.delimiter
            return s

