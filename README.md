---
title: Smart Inbox Env
sdk: docker
pinned: false
license: mit
short_description: 'It is a simulation of an email triage system '
---
**Smart Inbox Environment (OpenEnv)**

**Overview**
Smart Inbox Environment is a real-world simulation of an email triage system where an AI agent processes incoming emails and decides how to handle them.

The agent performs three key tasks:

* **Classify emails** (spam, important, normal)
* **Choose an action** (reply, ignore, escalate)
* **Generate responses** when required

This environment is designed to evaluate AI decision-making in realistic business communication workflows.

---

**Motivation**
In real-world organizations, employees constantly manage emails by:

* Filtering spam
* Responding to important queries
* Escalating urgent issues

This project simulates that workflow and provides a structured environment to train and evaluate intelligent agents.

---

**Environment Design**

The environment follows the OpenEnv interface:
* `reset(task)` → provides a new email
* `step(action)` → evaluates the agent’s decision
* `state()` → returns current environment state

Each episode represents handling one email.

---

**Observation Space**
Each observation contains structured email data:
* `email_id` — unique identifier
* `sender` — email sender
* `subject` — subject line
* `body` — email content
* `timestamp` — time received
* `priority_hint` — optional urgency indicator

---

**Action Space**

The agent must return:

* `classification` → `spam | important | normal`
* `action` → `reply | ignore | escalate`
* `response` → optional text (required for replies)

---

## Tasks

The environment includes three levels of difficulty:

### Easy

* Objective: Classify the email correctly
* Evaluation: Binary (0 or 1)

---

### Medium

* Objective: Classify the email and choose correct action
* Evaluation: Partial scoring

---

### Hard

* Objective: Full email handling

  * Classification
  * Action selection
  * Response generation
* Evaluation: Weighted scoring (0.0–1.0)

---

##  Reward Function

The reward score ranges from **0.0 to 1.0**, based on:

* Classification correctness → **+0.3**
* Action correctness → **+0.3**
* Response quality → **+0.4**

This allows **partial credit** instead of binary evaluation.

---

## Baseline Agent

A rule-based baseline agent is implemented using keyword heuristics.

It detects:

* Spam indicators (e.g., "win", "lottery", "offer")
* Urgent issues (e.g., "crash", "outage")
* User requests (e.g., "refund", "deadline")

This ensures:

* Deterministic behavior
* Reproducible results
* No dependency on external APIs

---

## Example Output

```
EASY SCORE: 0.8
MEDIUM SCORE: 0.7
HARD SCORE: 0.6

FINAL EVALUATION
Average Score: 0.7
Performance: Good
```

---

## How to Run Locally

```bash
cd smart_inbox_env
python baseline.py
```

---

## Docker Setup

Build the container:

```bash
docker build -t smart-inbox-env .
```

Run the container:

```bash
docker run smart-inbox-env
```

## Deployment

The environment is containerized using Docker and deployed on **Hugging Face Spaces**.

This ensures:

* Reproducibility
* Cloud execution
* Platform independence

---

## Project Structure

```
smart_inbox_env/
│
├── env/
│   ├── models.py        # Data models
│   ├── environment.py   # Core environment logic
│   ├── tasks.py         # Tasks and graders
│
├── inference.py          # Baseline agent
├── openenv.yaml         # OpenEnv configuration
├── Dockerfile           # Container setup
|── app.py               # contains API server
├── README.md            # Documentation
```

## Key Features

* Real-world task simulation (email triage)
* OpenEnv-compliant architecture
* Multi-level tasks with deterministic graders
* Continuous reward system (0.0–1.0)
* Reproducible baseline agent
* Docker-based deployment

---

## Future Improvements

* Expand dataset with more diverse emails
* Integrate LLM-based agents
* Improve response quality evaluation
* Add multi-email workflows

---

## Summary
This project demonstrates how AI agents can be evaluated in realistic environments involving classification, decision-making, and response generation.
It provides a scalable foundation for building intelligent assistants for real-world communication systems.

---

