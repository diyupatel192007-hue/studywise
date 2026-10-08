from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "study_data.csv"
MODEL_PATH = BASE_DIR / "model.pkl"
FEATURE_COLUMNS = [
    "study_hours",
    "sleep_hours",
    "phone_hours",
    "breaks",
    "exercise_hours",
    "focus_level",
    "stress_level",
    "attendance",
]
TARGET_COLUMN = "efficiency"


def load_dataset(dataset_path: Path = DATA_PATH) -> pd.DataFrame:
    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found at: {dataset_path}")

    data = pd.read_csv(dataset_path)
    if data.empty:
        raise ValueError("The dataset is empty.")

    required_columns = FEATURE_COLUMNS + [TARGET_COLUMN]
    missing_columns = [column for column in required_columns if column not in data.columns]
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {missing_columns}")

    numeric_columns = required_columns
    converted = data[numeric_columns].apply(pd.to_numeric, errors="raise")
    data[numeric_columns] = converted

    if data[numeric_columns].isnull().any().any():
        raise ValueError("Dataset contains missing values in required columns.")

    return data


def train_model(data: pd.DataFrame):
    X = data[FEATURE_COLUMNS]
    y = data[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("Model Training Completed!")
    print(f"Mean Absolute Error: {mae:.2f}")
    print(f"R2 Score: {r2:.2f}")

    joblib.dump(model, MODEL_PATH)
    print(f"Model saved as {MODEL_PATH.name}")
    return model


def main() -> None:
    data = load_dataset()
    train_model(data)


if __name__ == "__main__":
    main()