from datetime import datetime
import os
import networksecurity.constant import training_pipeline 
from sqlite3.dbapi2 import Timestamp

print("Network Security Config Entity Module Loaded")
print("Training Pipeline Name : ", training_pipeline.PIPELINE_NAME)


class TraningPipelineConfig:
    def __init__(self):
        
        self.PIPELINE_NAME = training_pipeline.PIPELINE_NAME
        self.ARTIFACT_DIR = training_pipeline.ARTIFACT_DIR
        self.CURRENT_TIME_STAMP = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.PIPELINE_ARTIFACT_DIR = os.path.join(self.ARTIFACT_DIR, self.CURRENT_TIME_STAMP)
        self.TRAINING_PIPELINE_CONFIG_FILE_PATH = os.path.join(self.PIPELINE_ARTIFACT_DIR, "training_pipeline_config.json")
        
class DataIngestionConfig:
    def __init__(self,TraningPipelineConfig: TraningPipelineConfig):
        self.traning_pipeline_config = TraningPipelineConfig
        self.data_ingestion_dir = os.path.join(
            TraningPipelineConfig.PIPELINE_ARTIFACT_DIR, 
            training_pipeline.DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path = os.path.join(
            self.data_ingestion_dir, 
            training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, 
            training_pipeline.FILE_NAME)
        self.training_file_path = os.path.join(
            self.data_ingestion_dir, 
            training_pipeline.DATA_INGESTION_INGESTED_DIR, 
            training_pipeline.TRAIN_FILE_NAME)
        self.testing_file_path = os.path.join(
            self.data_ingestion_dir, 
            training_pipeline.DATA_INGESTION_INGESTED_DIR, 
            training_pipeline.TEST_FILE_NAME)
        self.train_test_split_ratio = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name = training_pipeline.DATA_INGESITION_COLLECTION_NAME
        self.database_name = training_pipeline.DATA_INGESTION_DATABASE_NAME
        