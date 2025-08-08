from Teen_Phone_Addiction import logger
from Teen_Phone_Addiction.pipeline.stage_01_ingestion_data import (
    DataIngestionTrainingPipeline,
)
from Teen_Phone_Addiction.pipeline.stage_02_validation_data import (
    DataValidationTrainingPipeline,
)
from Teen_Phone_Addiction.pipeline.stage_03_transformation_data import (
    DataTransformationTrainingPipeline,
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


Stage_name = "Data Validation stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>> stage {Stage_name} started <<<<<<<<<<<<")
        data_ingestion = DataValidationTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>>>>>>> stage {Stage_name} completed <<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

Stage_name = "Data Transformation stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>> stage {Stage_name} started <<<<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>> stage {Stage_name} completed <<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
