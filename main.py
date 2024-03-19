from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainigPipeline
from cnnClassifier.pipeline.stage_03_preapase_training import ModelTrainingPipeline


STAGE_NAME ="Data Ingestion stage"
try:
    logger.info(f">>>>>>>>> stage{STAGE_NAME} started <<<<<<")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<< \n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare_base model"
try:
    logger.info(f"************************")
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    prepare_base_model= PrepareBaseModelTrainigPipeline()
    prepare_base_model.main()
    logger.info(f" >>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e