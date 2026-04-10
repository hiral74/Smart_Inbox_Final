from pydantic import BaseModel, Field
from typing import Optional, Literal


# -----------------------------
# Observation Model
# -----------------------------
class EmailObservation(BaseModel):
    email_id: str = Field(..., description="Unique email identifier")
    sender: str = Field(..., description="Email sender address")
    subject: str = Field(..., description="Email subject line")
    body: str = Field(..., description="Email body content")
    timestamp: str = Field(..., description="Time the email was received")
    priority_hint: Optional[Literal["low", "medium", "high"]] = Field(
        None, description="Optional priority hint"
    )


# -----------------------------
# Action Model
# -----------------------------
class EmailAction(BaseModel):
    classification: Literal["spam", "important", "normal"] = Field(
        ..., description="Email classification"
    )
    action: Literal["reply", "ignore", "escalate"] = Field(
        ..., description="Action to take"
    )
    response: Optional[str] = Field(
        None, description="Response text if replying"
    )


# -----------------------------
# Reward Model
# -----------------------------
class EmailReward(BaseModel):
    score: float = Field(..., ge=0.0, le=1.0, description="Reward score (0 to 1)")
    feedback: str = Field(..., description="Explanation of reward")