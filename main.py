from Teen_Phone_Addiction import logger
from Teen_Phone_Addiction.pipeline.stage_01_ingestion_data import (
    DataIngestionTrainingPipeline,
)

Stage_name = "Data Ingestion stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>> stage {Stage_name} started <<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>> stage {Stage_name} completed <<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
