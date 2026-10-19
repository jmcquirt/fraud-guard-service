def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "fraud-guard"}


def test_predict_valid_payload(client, valid_transaction_payload):
    response = client.post("/predict", json=valid_transaction_payload)
    assert response.status_code == 200

    data = response.json()
    assert "results" in data
    assert data["total_processed"] == 1
    assert "batch_latency_ms" in data

    # Check the nested result structure
    result = data["results"][0]
    assert result["transaction_id"] == "123e4567-e89b-12d3-a456-426614174000"
    assert "is_anomaly" in result
    assert "anomaly_score" in result


def test_predict_invalid_amount(client, valid_transaction_payload):
    # Mutate the payload to have a negative amount
    bad_payload = valid_transaction_payload.copy()
    bad_payload["transactions"][0]["amount"] = -50.00

    response = client.post("/predict", json=bad_payload)
    assert response.status_code == 422  # Unprocessable Entity (Pydantic validation error)

    data = response.json()
    assert "detail" in data
    assert data["detail"][0]["msg"] == "Input should be greater than 0"
