import os
import sys
import numpy as np
import  pandas as pd


"""
DATA INGESTION CONSTANTS
This module contains constants used in the data ingestion process of the Network Security project.
"""

TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "network_security"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


DATA_INGESITION_COLLECTION_NAME = "phishing_data"
DATA_INGESTION_DATABASE_NAME = "network_security"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float =   0.2
