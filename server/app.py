from env.environment import SmartInboxEnv
from env.models import EmailAction

app = FastAPI()
env = SmartInboxEnv()

@app.get("/")
def root():
    return {"message": "Smart Inbox OpenEnv running"}

@app.post("/reset")
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