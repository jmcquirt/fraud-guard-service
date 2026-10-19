from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class ServiceSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="FRAUD_", env_file=".env", extra="ignore")

    app_name: str = "Fraud Anomaly Detection Service"
    environment: str = "production"
    log_level: str = "INFO"

    # Path to serialized Scikit-Learn pipeline
    model_artifact_path: str = "artifacts/D804_PA_Model_Credit_Card_Fraud.joblib"

    # Operational decision boundary
    anomaly_score_threshold: float = Field(
        default=-45.0,
        description="Log-likelihood threshold below which a transaction is flagged as an anomaly"
    )

settings = ServiceSettings()