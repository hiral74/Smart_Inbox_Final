from fastapi import FastAPI
from env.environment import SmartInboxEnv
from env.models import EmailAction
from inference import main   # ✅ ADD THIS IMPORT

app = FastAPI()

@app.on_event("startup")
def startup_event():
    print("SERVER STARTED", flush=True)

env = SmartInboxEnv()

# -----------------------------
# Routes
# -----------------------------

@app.get("/")
def root():
    return {"message": "Smart Inbox OpenEnv running"}


@app.get("/reset")
def reset(task: str = "easy"):
    obs = env.reset(task)
    return obs.dict()


@app.post("/step")
def step(action: dict):
    action_obj = EmailAction(**action)
    obs, reward, done, info = env.step(action_obj)

    return {
        "observation": obs.dict(),
        "reward": reward.dict(),
        "done": done,
        "info": info
    }


# ✅ ADD THIS AT THE BOTTOM
@app.get("/run")
def run_agent():
    main()
    return {"status": "agent finished"}
