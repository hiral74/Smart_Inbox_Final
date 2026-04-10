from typing import Tuple, Dict, Any
import random

from env.models import EmailObservation, EmailAction, EmailReward
from .tasks import EasyTask, MediumTask, HardTask


class SmartInboxEnv:
    def __init__(self):
        self.current_email = None
        self.done = False
        self.step_count = 0
        self.current_task = "easy"

        # Task registry
        self.tasks = {
            "easy": EasyTask(),
            "medium": MediumTask(),
            "hard": HardTask()
        }

        # Sample dataset 
        self.emails = [
            {
                "email_id": "E001",
                "sender": "customer@gmail.com",
                "subject": "Refund not received",
                "body": "I have not received my refund for order #123.",
                "timestamp": "2026-04-04T10:00:00",
                "priority_hint": "high",
                "ground_truth": {
                    "classification": "important",
                    "action": "reply"
                }
            },
            
            {
                "email_id": "E002",
                "sender": "spam@offers.com",
                "subject": "WIN A FREE iPhone!!!",
                "body": "Click here to claim your prize",
                "timestamp": "2026-04-04T11:00:00",
                "priority_hint": "low",
                "ground_truth": {
                    "classification": "spam",
                    "action": "ignore"
                }
            },
            {
                "email_id": "E003",
                "sender": "boss@company.com",
                "subject": "Meeting reschedule",
                "body": "Let’s move the meeting to 3 PM.",
                "timestamp": "2026-04-04T12:00:00",
                "priority_hint": "high",
                "ground_truth": {
                    "classification": "important",
                    "action": "reply"
                }
            },
            {
                "email_id": "E004",
                "sender": "support@bank.com",
                "subject": "Verify your account immediately",
                "body": "Your account will be suspended unless you verify your details.",
                "timestamp": "2026-04-04T13:00:00",
                "priority_hint": "high",
                "ground_truth": {
                    "classification": "spam",
                    "action": "ignore"
                }
            },
            {
                "email_id": "E005",
                "sender": "friend@gmail.com",
                "subject": "Dinner this weekend?",
                "body": "Hey, are you free for dinner on Saturday?",
                "timestamp": "2026-04-04T14:00:00",
                "priority_hint": "low",
                "ground_truth": {
                    "classification": "normal",
                    "action": "ignore"
                }
            },
            {
                "email_id": "E006",
                "sender": "it-support@company.com",
                "subject": "System outage reported",
                "body": "Multiple users report system crash. Immediate attention required.",
                "timestamp": "2026-04-04T15:00:00",
                "priority_hint": "high",
                "ground_truth": {
                    "classification": "important",
                    "action": "escalate"
                }
            },
            {
                "email_id": "E007",
                "sender": "newsletter@shopping.com",
                "subject": "Exclusive deals just for you",
                "body": "Check out our latest offers and discounts.",
                "timestamp": "2026-04-04T16:00:00",
                "priority_hint": "low",
                "ground_truth": {
                    "classification": "spam",
                    "action": "ignore"
                }
            },
            {
                "email_id": "E008",
                "sender": "hr@company.com",
                "subject": "Interview schedule confirmation",
                "body": "Please confirm your availability for the interview tomorrow.",
                "timestamp": "2026-04-04T17:00:00",
                "priority_hint": "high",
                "ground_truth": {
                    "classification": "important",
                    "action": "reply"
                }
            },
            {
                "email_id": "E009",
                "sender": "unknown@random.com",
                "subject": "You won a lottery!",
                "body": "Claim your prize now by clicking this link.",
                "timestamp": "2026-04-04T18:00:00",
                "priority_hint": "low",
                "ground_truth": {
                    "classification": "spam",
                    "action": "ignore"
                }
            },
            {
                "email_id": "E010",
                "sender": "teamlead@company.com",
                "subject": "Project deadline update",
                "body": "Deadline moved to next Friday. Please acknowledge.",
                "timestamp": "2026-04-04T19:00:00",
                "priority_hint": "medium",
                "ground_truth": {
                    "classification": "important",
                    "action": "reply"
                }
            },
            {
                "email_id": "E011",
                "sender": "alerts@server.com",
                "subject": "High CPU usage detected",
                "body": "Server CPU usage exceeded 95%. Immediate action required.",
                "timestamp": "2026-04-04T20:00:00",
                "priority_hint": "high",
                "ground_truth": {
                    "classification": "important",
                    "action": "escalate"
                }
            },
            {
                "email_id": "E012",
                "sender": "colleague@company.com",
                "subject": "Can you review this doc?",
                "body": "Please review the attached document when you have time.",
                "timestamp": "2026-04-04T21:00:00",
                "priority_hint": "medium",
                "ground_truth": {
                    "classification": "normal",
                    "action": "ignore"
                }
            },
            {
                "email_id": "E013",
                "sender": "security@bank.com",
                "subject": "Suspicious login attempt",
                "body": "We detected a login from a new device. Please confirm if this was you.",
                "timestamp": "2026-04-04T22:00:00",
                "priority_hint": "high",
                "ground_truth": {
                    "classification": "important",
                    "action": "reply"
                }
            
            },
            {
                "email_id": "E014",
                "sender": "promo@travel.com",
                "subject": "Limited time flight discounts",
                "body": "Book your tickets now and save up to 50% on flights.",
                "timestamp": "2026-04-04T23:00:00",
                "priority_hint": "low",
                "ground_truth": {
                    "classification": "spam",
                    "action": "ignore"
                }
            },
            {
                "email_id": "E015",
                "sender": "manager@company.com",
                "subject": "Urgent: Client meeting prep",
                "body": "Please prepare the slides for tomorrow’s client meeting ASAP.",
                "timestamp": "2026-04-05T09:00:00",
                "priority_hint": "high",
                "ground_truth": {
                    "classification": "important",
                    "action": "reply"
                }
            },
            {
                "email_id": "E016",
                "sender": "no-reply@subscriptions.com",
                "subject": "Your subscription is expiring",
                "body": "Renew your subscription to continue enjoying our services.",
                "timestamp": "2026-04-05T10:00:00",
                "priority_hint": "medium",
                "ground_truth": {
                    "classification": "normal",
                    "action": "ignore"
                }
            },
            {
                "email_id": "E017",
                "sender": "alerts@security.com",
                "subject": "Multiple failed login attempts",
                "body": "We detected multiple failed login attempts. Please secure your account.",
                "timestamp": "2026-04-05T11:00:00",
                "priority_hint": "high",
                "ground_truth": {
                    "classification": "important",
                    "action": "escalate"
                }
            },
            {
                "email_id": "E018",
                "sender": "friend2@gmail.com",
                "subject": "Movie tonight?",
                "body": "Hey, want to catch a movie later today?",
                "timestamp": "2026-04-05T12:00:00",
                "priority_hint": "low",
                "ground_truth": {
                    "classification": "normal",
                    "action": "ignore"
                }
            },
            {
                "email_id": "E019",
                "sender": "support@ecommerce.com",
                "subject": "Order delayed",
                "body": "Your order has been delayed due to unforeseen circumstances.",
                "timestamp": "2026-04-05T13:00:00",
                "priority_hint": "medium",
                "ground_truth": {
                    "classification": "important",
                    "action": "reply"
                }
            },
            {
                "email_id": "E020",
                "sender": "offers@casino.com",
                "subject": "Win big rewards now!",
                "body": "Join now and win exciting prizes instantly.",
                "timestamp": "2026-04-05T14:00:00",
                "priority_hint": "low",
                "ground_truth": {
                    "classification": "spam",
                    "action": "ignore"
                }
            }
        ]

    # -----------------------------
    # RESET
    # -----------------------------
    def reset(self, task: str = "easy") -> EmailObservation:
        if task not in self.tasks:
            raise ValueError(f"Invalid task: {task}")

        self.current_task = task
        self.current_email = random.choice(self.emails)
        self.done = False
        self.step_count = 0

        return EmailObservation(
            email_id=self.current_email["email_id"],
            sender=self.current_email["sender"],
            subject=self.current_email["subject"],
            body=self.current_email["body"],
            timestamp=self.current_email["timestamp"],
            priority_hint=self.current_email["priority_hint"],
        )

    # -----------------------------
    # STEP
    # -----------------------------
    def step(
        self, action: EmailAction
    ) -> Tuple[EmailObservation, EmailReward, bool, Dict[str, Any]]:
        if self.done:
            raise Exception("Episode already finished. Call reset().")

        self.step_count += 1

        gt = self.current_email["ground_truth"]

        # Select task grader
        task = self.tasks[self.current_task]

        # Compute score using task-specific grader
        score = task.grade(action, gt)

        # Clamp score between 0 and 1
        score = max(0.0, min(1.0, score))

        reward = EmailReward(
            score=score,
            feedback=f"Task: {self.current_task}"
        )

        self.done = True

        # Terminal observation
        next_obs = EmailObservation(
            email_id="END",
            sender="",
            subject="",
            body="",
            timestamp="",
            priority_hint=None
        )

        info = {
            "ground_truth": gt,
            "task": self.current_task
        }

        return next_obs, reward, self.done, info

    # -----------------------------
    # STATE
    # -----------------------------
    def state(self) -> Dict[str, Any]:
        return {
            "current_email": self.current_email,
            "task": self.current_task,
            "step_count": self.step_count,
            "done": self.done
        }