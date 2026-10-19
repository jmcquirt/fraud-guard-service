from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.config import settings
from src.services.preprocessor import FraudPreprocessor
from src.services.detector import AnomalyDetector
from src.api.routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.preprocessor = FraudPreprocessor()
    app.state.detector = AnomalyDetector(
        pipeline_path=settings.model_artifact_path, 
        threshold=settings.anomaly_score_threshold
    )
    yield
    app.state.preprocessor = None
    app.state.detector = None

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router)