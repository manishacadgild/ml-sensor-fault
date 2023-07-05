from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipeLineConfig,DataIngestionConfig

from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline



if __name__=='__main__':
    #mongodb_client=MongoDBClient()
    #print("collection name:",mongodb_client.database.list_collection_names())
    #training_pipeline_config=TrainingPipeLineConfig()
    #data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    #print(data_ingestion_config.__dict__)
    training_pipeline=TrainPipeline()
    training_pipeline.run_pipeline()
    