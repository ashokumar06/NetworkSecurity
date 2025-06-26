from networksecurity.logging.logger import logger
from networksecurity.exception.exception import NetworkSecurityException
import sys
from networksecurity.entity.config_entity import DataValidationArtifact
from networksecurity.entity.artifact_entity import DataInputArtifact
import pandas as pd
import os
from scipy.stats import ks_2samp