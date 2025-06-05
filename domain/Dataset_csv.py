from domain.Dataset import DataSet
import pandas as pd

class DataSetCSV(DataSet):

    def __init__(self, source):
        super.__init__(source)

    def dataCharger(self):
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