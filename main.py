from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger
from networksecurity.entity.config_entity import TraningPipelineConfig, DataIngestionConfig

import sys

if __name__ == "__main__":
    try:
        traning_pipeline_config = TraningPipelineConfig()
        data_ingestion_config = DataIngestionConfig(traning_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)

        logger.info(f"Data ingestion artifact: {data_ingestion_config}")
     
        data_input_artifact = data_ingestion.initiate_data_ingestion()
        logger.info(f"Data Ingestion Artifact: {data_input_artifact}")
        print(f"Data Ingestion Artifact: {data_input_artifact}")
    except Exception as e:
        logger.exception("Exception occurred in the main block")
        _, _, exc_tb = sys.exc_info()
        raise NetworkSecurityException(str(e), exc_tb) from e

