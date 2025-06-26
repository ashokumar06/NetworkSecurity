from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import certifi
import os 
import sys 
import json
from setuptools.config._validate_pyproject.formats import RECOMMEDED_ENTRYPOINT_PATTERN

load_dotenv()

uri = os.getenv("MONGODB_URI")

ca = certifi.where()


import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logger
from networksecurity.exception.exception import NetworkSecurityException



class NetworkDataExtract():
    """
    Class to extract network data from MongoDB and save it as a CSV file.
    """

    def __init__(self):
        try:
            pass
        except Exception as e:
            _, _, exc_tb = sys.exc_info()
            raise NetworkSecurityException(str(e), exc_tb)

    def csv_to_json(self, csv_file_path: str):

        try:
            df = pd.read_csv(csv_file_path)
            df.reset_index(drop=True, inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            _, _, exc_tb = sys.exc_info()
            raise NetworkSecurityException(str(e), exc_tb)

    def push_data(self, records, database, colection):
        try:
            self.database = database
            self.colection = colection
            self.records = records
            self.client = MongoClient(uri, tlsCAFile=ca)
            self.database = self.client[self.database]
            self.colection = self.database[self.colection]
            self.colection.insert_many(self.records)

            logger.info(f"Data pushed to {self.colection} collection in {self.database} database successfully.")

            return True
        
        except Exception as e:
            _, _, exc_tb = sys.exc_info()
            raise NetworkSecurityException(str(e), exc_tb)
 
if __name__ == "__main__":
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "network_security"
    COLECTION = "phishing_data"
    try:
        network_data_extract = NetworkDataExtract()
        records = network_data_extract.csv_to_json(FILE_PATH)
        network_data_extract.push_data(records, DATABASE, COLECTION)
    except NetworkSecurityException as e:
        logger.error(e)
        print(e)
        sys.exit(1)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

