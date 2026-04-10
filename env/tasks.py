from typing import Dict, Any
from .models import EmailAction


# -----------------------------
# EASY TASK -- Did the AI correctly understand the email?”
# -----------------------------
class EasyTask:
    name = "easy_classification"

    def grade(self, action: EmailAction, ground_truth: Dict[str, Any]) -> float:
        if action.classification == ground_truth["classification"]:
            return 0.95
        return 0.05


# -----------------------------
# MEDIUM TASK -- Did the AI correctly understand the email + suggest an appropriate action?”
# -----------------------------
class MediumTask:
    name = "medium_classification_action"

    def grade(self, action: EmailAction, ground_truth: Dict[str, Any]) -> float:
        score = 0.0

        if action.classification == ground_truth["classification"]:
            score += 0.5

        if action.action == ground_truth["action"]:
            score += 0.5
            
        score=max(0.05,min(0.95,score))
        return score


# -----------------------------
# HARD TASK -- Did the AI correctly understand the email + suggest an appropriate action + provide a high-quality response?
# -----------------------------
class HardTask:
    name = "hard_full_email_handling"

    def grade(self, action: EmailAction, ground_truth: Dict[str, Any]) -> float:
        score = 0.0

        # Classification
        if action.classification == ground_truth["classification"]:
            score += 0.3

        # Action
        if action.action == ground_truth["action"]:
            score += 0.3

        # Response quality 
        if ground_truth["action"] == "reply":
            if action.response and len(action.response) > 15:
                score += 0.4
        score=max(0.05,min(0.95,score))
        return score
