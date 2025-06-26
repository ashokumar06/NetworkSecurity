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
from networksecurity.entity.artifact_entity import DataInputArtifact

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

            if "_id" in dataframe.columns:
                dataframe = dataframe.drop(columns=["_id"])

            if dataframe.empty:
                raise NetworkSecurityException("No data found in the collection.")
            
            logger.info("Data Exported Successfully")

            dataframe.replace([np.inf, -np.inf], np.nan, inplace=True)

            return dataframe
        
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    def export_data_to_feature_store(self, dataframe: pd.DataFrame):
        try:
            logger.info("Exporting Data to Feature Store")
            os.makedirs(os.path.dirname(self.data_ingestion_config.feature_store_file_path), exist_ok=True)
            dataframe.to_csv(self.data_ingestion_config.feature_store_file_path, index=False)
            logger.info("Data Exported to Feature Store Successfully")
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    def split_data_as_train_test(self):
        try:
            logger.info("Splitting Data into Train and Test Sets")


            dataframe = pd.read_csv(self.data_ingestion_config.feature_store_file_path)
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio, random_state=42)

            os.makedirs(os.path.dirname(self.data_ingestion_config.training_file_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.data_ingestion_config.testing_file_path), exist_ok=True)

            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False)

            logger.info("Data Split into Train and Test Sets Successfully")
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e    
    
    def initiate_data_ingestion(self):
        try:
            logger.info("Starting Data Ingestion")
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_data_to_feature_store(dataframe)

            self.split_data_as_train_test()
            data_input_artifact = DataInputArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )

            logger.info("Data Ingestion Completed Successfully")

            return data_input_artifact
        
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    

