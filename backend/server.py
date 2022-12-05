from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
from error_handler import error_handler
from vcs_api.vcs_factory import create_vcs_connector
from extract_files.extract_by_libraries import extract_by_libraries_ast
from extract_files.function_finder import find_function
app = FastAPI()


@app.post("/files", status_code=status.HTTP_201_CREATED)
async def get_files(request: Request):
    try:
        result: dict = await request.json()
        error_handler.post_request(client_data=result)
        org = create_vcs_connector(token=result["token"], organization=result["organization"], vcs_type=result["vcs_type"])
        files = extract_by_libraries_ast(org.get_files_from_organization(), ["hashlib", "bycrypt"])
        for file in files:
            find_function(file["file"].decoded_content.decode("utf-8"))
    except ValueError as error:
        print(error)
    return 0


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
