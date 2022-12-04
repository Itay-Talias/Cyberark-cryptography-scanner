from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from error_handler import error_handler
from vcs_api.vcs_factory import create_vcs_connector
from extract_files.extract_by_libraries import extract_by_libraries, extract_by_libraries_ast
app = FastAPI()


@app.post("/files", status_code=status.HTTP_201_CREATED)
async def get_files(request: Request) -> list[object]:
    try:
        result: dict = await request.json()
        error_handler.post_request(client_data = result)
        org = create_vcs_connector(token=result["token"], organization=result["organization"], vcs_type=result["vcs_type"])
        return extract_by_libraries_ast(org.get_files_from_organization(), ["hashlib"])
    except ValueError as error:
        print(error)
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)


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
