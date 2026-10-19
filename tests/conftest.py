import pytest
from fastapi.testclient import TestClient

from src.api.main import app


@pytest.fixture(scope="module")
def client():
    # Use the TestClient within the lifespan context to load the ML model
    with TestClient(app) as c:
        yield c


@pytest.fixture
def valid_transaction_payload():
    return {
        "transactions": [
            {
                "transaction_id": "123e4567-e89b-12d3-a456-426614174000",
                "amount": 150.00,
                "v1": -1.359807,
                "v2": -0.072781,
                "v3": 2.536347,
                "v4": 1.378155,
                "v5": -0.338321,
                "v6": 0.462388,
                "v7": 0.239599,
                "v8": 0.098698,
                "v9": 0.363787,
                "v10": 0.090794,
                "v11": -0.551600,
                "v12": -0.617801,
                "v13": -0.991390,
                "v14": -0.311169,
                "v15": 1.468177,
                "v16": -0.470401,
                "v17": 0.207971,
                "v18": 0.025791,
                "v19": 0.403993,
                "v20": 0.251412,
                "v21": -0.018307,
                "v22": 0.277838,
                "v23": -0.110474,
                "v24": 0.066928,
                "v25": 0.128539,
                "v26": -0.189115,
                "v27": 0.133558,
                "v28": -0.021053,
            }
        ]
    }
