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

"""
Data Validation Constants
This module contains constants used in the data validation process of the Network Security project.
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_Valid_DIR: str = "valid_data"
DATA_VALIDATION_INVALID_DIR: str = "invalid_data"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME: str = "report.html"
