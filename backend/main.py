from fastapi import FastAPI

app= FastAPI(title="AgentHound")

@app.get("/")
def root():
    return{"message": "AgentHound API is running"}