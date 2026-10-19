import time
import joblib
import numpy as np
from src.schemas.payload import TransactionPayload
from src.schemas.response import AnomalyDecision, BatchAnomalyDecision


class AnomalyDetector:
    def __init__(self, pipeline_path: str, threshold: float):
        self.pipeline = joblib.load(pipeline_path)
        self.threshold = threshold

    def predict_batch(
        self, transactions: list[TransactionPayload], feature_matrix: np.ndarray
    ) -> BatchAnomalyDecision:
        start_time = time.perf_counter()

        # Scikit-Learn pipeline handles Imputer -> Yeo-Johnson -> BGM
        log_likelihoods = self.pipeline.score_samples(feature_matrix)

        decisions = []
        anomalies_count = 0

        for tx, score in zip(transactions, log_likelihoods):
            is_anomaly = bool(score < self.threshold)
            if is_anomaly:
                anomalies_count += 1

            decisions.append(
                AnomalyDecision(
                    transaction_id=tx.transaction_id,
                    is_anomaly=is_anomaly,
                    anomaly_score=float(score),
                    threshold_applied=self.threshold,
                    latency_ms=0.0,
                )
            )

        end_time = time.perf_counter()
        batch_latency_ms = (end_time - start_time) * 1000.0

        avg_latency_ms = batch_latency_ms / len(transactions)
        for decision in decisions:
            decision.latency_ms = round(avg_latency_ms, 3)

        return BatchAnomalyDecision(
            results=decisions,
            total_processed=len(transactions),
            total_anomalies=anomalies_count,
            batch_latency_ms=round(batch_latency_ms, 3),
        )
