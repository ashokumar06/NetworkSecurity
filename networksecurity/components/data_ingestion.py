from networksecurity.logging.logger import logger
from networksecurity.exception.exception import NetworkSecurityException
import pandas as pd
import json
import numpy as np
import pymongo 
import sys  

# # configuration of data ingestion

from networksecurity.entity.config_entity import DataIngestionConfig
from typing import List
from sklearn.model_selection import train_test_split
import os

from dotenv import load_dotenv
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")


class DataIngestion:
    def __init__(self, data_ingesition_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingesition_config
            logger.info("Data Ingestion Module Initialized")
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    def export_collection_as_dataframe(self) -> pd.DataFrame:
        try:
            logger.info("Exporting MongoDB Collection as DataFrame")
            client = pymongo.MongoClient(MONGODB_URI)
            database = client[self.data_ingestion_config.database_name]
            collection = database[self.data_ingestion_config.collection_name]
            documents = collection.find()
            dataframe = pd.DataFrame(list(documents))
            if dataframe.empty:
                raise NetworkSecurityException("No data found in the collection.")
            logger.info("Data Exported Successfully")
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    def initiate_data_ingestion(self):
        try:
            logger.info("Starting Data Ingestion")
            dataframe = self.export_collection_as_dataframe()
            self.split_data_as_train_test()
            logger.info("Data Ingestion Completed Successfully")
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e