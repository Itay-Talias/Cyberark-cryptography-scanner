from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import List
from vcs_api.github_api import get_files_from_organization
from error_handler import error_handler


app = FastAPI()

@app.post("/files", status_code=status.HTTP_201_CREATED)
async def get_files(request: Request) -> List[dict]:
    try:
        result: dict = await request.json()
        error_handler.post_request(client_data = result)
        files = get_files_from_organization(result.token,result.organization)
    except Exception as error:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)
    return files


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return "server is running"


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)