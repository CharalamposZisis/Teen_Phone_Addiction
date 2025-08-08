import os
from Teen_Phone_Addiction import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from Teen_Phone_Addiction.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config, df, target_column):
        self.config = config
        self.df = df
        self.target_column = target_column
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=0.95)

    def preprocess(self):
        # Drop non-numeric/identifier columns
        drop_cols = ["ID", "Name", "Location", "School_Grade"]
        features = self.df.drop(columns=drop_cols + [self.target_column])
        target = self.df[self.target_column]

        # Scale
        scaled_data = self.scaler.fit_transform(features)

        # PCA
        x_pca = self.pca.fit_transform(scaled_data)

        return x_pca, target

    def train_test_split_and_save(self):
        X, y = self.preprocess()

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Convert to DataFrames for saving
        train_df = pd.DataFrame(X_train)
        train_df["target"] = y_train.reset_index(drop=True)

        test_df = pd.DataFrame(X_test)
        test_df["target"] = y_test.reset_index(drop=True)

        os.makedirs(self.config.root_dir, exist_ok=True)
        train_df.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test_df.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        print(f"Train shape: {train_df.shape}, Test shape: {test_df.shape}")
