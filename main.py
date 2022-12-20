from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.logger import logging
import os,sys



if __name__== '__main__':
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()
