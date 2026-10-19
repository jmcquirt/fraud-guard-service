import numpy as np

from src.schemas.payload import TransactionPayload


class FraudPreprocessor:
    def __init__(self):
        pass

    def transform(self, transactions: list[TransactionPayload]) -> np.ndarray:
        feature_matrix = np.zeros((len(transactions), 29))

        for i, tx in enumerate(transactions):
            # V1 through V28 must go first (indices 0 to 27)
            feature_matrix[i, 0:28] = [getattr(tx, f"v{j}") for j in range(1, 29)]
            # Amount must go last (index 28)
            feature_matrix[i, 28] = tx.amount

        return feature_matrix
