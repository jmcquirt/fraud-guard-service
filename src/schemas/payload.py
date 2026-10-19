import math
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator


class TransactionPayload(BaseModel):
    transaction_id: UUID = Field(default_factory=uuid4)
    amount: float = Field(..., gt=0.0, le=500000.0)

    # PCA components V1 to V28
    v1: float = Field(...)
    v2: float = Field(...)
    v3: float = Field(...)
    v4: float = Field(...)
    v5: float = Field(...)
    v6: float = Field(...)
    v7: float = Field(...)
    v8: float = Field(...)
    v9: float = Field(...)
    v10: float = Field(...)
    v11: float = Field(...)
    v12: float = Field(...)
    v13: float = Field(...)
    v14: float = Field(...)
    v15: float = Field(...)
    v16: float = Field(...)
    v17: float = Field(...)
    v18: float = Field(...)
    v19: float = Field(...)
    v20: float = Field(...)
    v21: float = Field(...)
    v22: float = Field(...)
    v23: float = Field(...)
    v24: float = Field(...)
    v25: float = Field(...)
    v26: float = Field(...)
    v27: float = Field(...)
    v28: float = Field(...)

    @field_validator("*", mode="before")
    @classmethod
    def reject_nan_and_inf(cls, value: float) -> float:
        # Combine the type check and the value check onto one line
        if isinstance(value, (int, float)) and (math.isnan(value) or math.isinf(value)):
            raise ValueError("NaN and Infinity are not permitted.")
        return value


class BatchTransactionPayload(BaseModel):
    transactions: list[TransactionPayload] = Field(..., min_length=1, max_length=500)
