from domain.Dataset import DataSet
import pandas as pd

class DataSetEXEL(DataSet):

    def __init__(self, source):
        super().__init__(source)

    def dataCharger(self):
        try:
            if self.extDevolution()==".xlsx" | self.extDevolution() == ".xls":
                df=pd.read_excel(self.source)
                self.data=df
                if self.dataValidation():
                    self.dataValidation()
                    print("exel cargado exitosamente")
            else:
                raise ValueError("error extencion no admitible, solo exels")
        except Exception as e:
            print(f"error en cargar exel, {e}")
    