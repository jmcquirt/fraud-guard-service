from uuid import UUID
from pydantic import BaseModel


class AnomalyDecision(BaseModel):
    transaction_id: UUID
    is_anomaly: bool
    anomaly_score: float
    threshold_applied: float
    latency_ms: float


class BatchAnomalyDecision(BaseModel):
    results: list[AnomalyDecision]
    total_processed: int
    total_anomalies: int
    batch_latency_ms: float
