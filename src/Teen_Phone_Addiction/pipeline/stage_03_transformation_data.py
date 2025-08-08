from Teen_Phone_Addiction.config.configuration import ConfigurationManager
from Teen_Phone_Addiction.components.data_transformation import DataTransformation
from Teen_Phone_Addiction import logger
from pathlib import Path


Stage_name = "Data Transformation stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1].strip()

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()

        except Exception as e:
            logger.exception(e)
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>> stage {Stage_name} started <<<<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>> stage {Stage_name} completed <<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
