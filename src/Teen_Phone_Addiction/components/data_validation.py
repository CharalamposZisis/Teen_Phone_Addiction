import os
from Teen_Phone_Addiction import logger
from Teen_Phone_Addiction.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data(self):
        try:
            validation_status = None

            df = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(df.columns)

            all_schema = self.config.all_schema.keys()

            for column in all_columns:
                if column not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation Status: {validation_status}\n")

                else:
                    validation_status = True
                    with open(self.config.status_file, "w") as f:
                        f.write(f"Validation Status: {validation_status}\n")

                return validation_status

        except Exception as e:
            raise e
