
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    r2_score,
    mean_squared_error,
    mean_absolute_error
)
import numpy as np


def load_and_split(
    path="../Dataset/Advertising.csv",
    test_size=0.2,
    random_state=42
):
    # Load dataset
    df = pd.read_csv(path, index_col=0)

    # Standardize column names
    df.columns = df.columns.str.lower()

    # Separate training and testing data
    df_train, df_test = train_test_split(
        df,
        test_size=test_size,
        random_state=random_state
    )

    return df_train, df_test


def eval_regression(y_true, y_pred):

    return {
        "R2": r2_score(y_true, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_true, y_pred)),
        "MAE": mean_absolute_error(y_true, y_pred)
    }
