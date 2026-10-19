from fastapi import Request
from src.services.preprocessor import FraudPreprocessor
from src.services.detector import AnomalyDetector


def get_preprocessor(request: Request) -> FraudPreprocessor:
    return request.app.state.preprocessor


def get_detector(request: Request) -> AnomalyDetector:
    return request.app.state.detector
