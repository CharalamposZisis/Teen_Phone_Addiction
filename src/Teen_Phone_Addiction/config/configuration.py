from Teen_Phone_Addiction.constants import *
from Teen_Phone_Addiction.utils.common import read_yaml, create_directories
from Teen_Phone_Addiction.entity.config_entity import (
    DataValidationConfig,
    DataIngestionConfig,
    DataTransformationConfig,
)


class ConfigurationManager:
    def __init__(
        self,
        config_file_path=CONFIG_FILE_PATH,
        params_file_path=PARAMS_FILE_PATH,
        schema_file_path=SCHEMA_FILE_PATH,
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            dataset_download_url=config.dataset_download_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([self.config.artifacts_root])

        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir), data_path=Path(config.data_path)
        )

        return data_transformation_config
