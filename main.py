from fastapi import FastAPI
from heplers.scraping import scrape_github_projects
from pydantic import BaseModel

class UserPayload(BaseModel):
    username: str

app = FastAPI()

@app.post("/scrape")
async def scrape_github(payload: UserPayload):
    return await scrape_github_projects(payload.username)