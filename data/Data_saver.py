import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from decouple import config

class DataSaver():
    def __init__(self):
        db=config("DB_NAME")
        user=config("DB_USER")
        password=config("DB_PASSWORD")
        host=config("DB_HOST")
        port=config("DB_PORT")
        
        url=f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
        self.engine=create_engine(url)

    def saveDataFrame(self, df, table_name):
        if (df is None | df.empty):
            print(" datos vacios en df")
            return
        if not isinstance(df, pd.DataFrame):
            print(f"error df no valido del tipo pandas, se recibio {type(df)}")
            return
        try:
            # consideraciones, la carga es unica por tabla, si quieres ingresar datos nuevos de 1 tabla
            # perderas los datos anteriores, para evitarlo remplza "replace" por "append"
            # el tratamiento de duplicados debera hacerse desde un gestor de db
            df.to_sql(name=table_name, con=self.engine, if_exists='replace', index=False)
            print("datos cargados correctamente")

        except SQLAlchemyError as e:
            print(f'error al intentar cargar datos, el error es: {e}')

