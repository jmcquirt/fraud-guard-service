from fastapi import APIRouter, Depends, HTTPException
from src.schemas.payload import BatchTransactionPayload
from src.schemas.response import BatchAnomalyDecision
from src.services.preprocessor import FraudPreprocessor
from src.services.detector import AnomalyDetector
from src.api.dependencies import get_preprocessor, get_detector

router = APIRouter()


@router.get("/health", tags=["System Observability"])
def health_check():
    return {"status": "healthy", "service": "fraud-guard"}


@router.post("/predict", response_model=BatchAnomalyDecision, tags=["Inference"])
def predict(
    payload: BatchTransactionPayload,
    preprocessor: FraudPreprocessor = Depends(get_preprocessor),
    detector: AnomalyDetector = Depends(get_detector),
):
    try:
        feature_matrix = preprocessor.transform(payload.transactions)
        decision = detector.predict_batch(payload.transactions, feature_matrix)
        return decision

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference failure: {str(e)}")
