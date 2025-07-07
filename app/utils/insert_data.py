import os

from database.models import Consumer, GDP

from database.session import SessionLocal

import pandas as pd

from sqlalchemy.exc import SQLAlchemyError

from utils.download import DownloadData


class DataInserter:
    def __init__(self) -> None:
        self.download = DownloadData()
        self.session = SessionLocal()
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.GPD_FILE_PATH = os.path.join(os.path.dirname(self.BASE_DIR), 'data/gdp.csv')
        self.CONSUMER_FILE_PATH = os.path.join(os.path.dirname(self.BASE_DIR), 'data/consumer.csv')
        
    def insert_gdp_data(self):
        df = pd.read_csv(self.GPD_FILE_PATH)
        # Harmoniser les noms de colonnes avec la table GDP
        df = df.rename(columns={
            'Country': 'country',
            'Country Code': 'country_code',
            'Year': 'year',
            'Inflation': 'inflation'
        })
        try:
            df.to_sql(
                GDP.__tablename__,
                con=self.session.bind,
                if_exists='append',
                index=False,
                dtype={
                    'country': GDP.country.type,
                    'country_code': GDP.country_code.type,
                    'year': GDP.year.type,
                    'inflation': GDP.inflation.type
                }
            )
            print("GDP data inserted successfully.")
        except SQLAlchemyError as e:
            print(f"Database error: {e}")

    def insert_consumer_data(self):
        # Lire le header pour avoir les bons noms de colonnes
        df = pd.read_csv(self.CONSUMER_FILE_PATH)
        df = df.rename(columns={
            'Country': 'country',
            'Country Code': 'country_code',
            'Year': 'year',
            'Inflation': 'inflation'
        })
        try:
            df.to_sql(
                Consumer.__tablename__,
                con=self.session.bind,
                if_exists='append',
                index=False,
                dtype={
                    'country': Consumer.country.type,
                    'country_code': Consumer.country_code.type,
                    'year': Consumer.year.type,
                    'inflation': Consumer.inflation.type
                }
            )
            print("Consumer data inserted successfully.")
        except SQLAlchemyError as e:
            print(f"Database error: {e}")

    def run(self):
        with self.session.begin():
            self.insert_gdp_data()
            self.insert_consumer_data()
            self.session.close()
