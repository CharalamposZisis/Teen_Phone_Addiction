from Teen_Phone_Addiction.config.configuration import ConfigurationManager
from Teen_Phone_Addiction.components.data_validation import DataValidation
from Teen_Phone_Addiction import logger


Stage_name = "Data Validation stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_data()


if __name__ == "main":
    try:
        logger.info(f">>>>>>>>>>>>> stage {Stage_name} started <<<<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>> stage {Stage_name} completed <<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
