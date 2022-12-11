from fastapi import FastAPI, status, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.responses import JSONResponse
from error_handler import error_handler
from vcs_api.vcs_factory import create_vcs_connector
from extract_files.extract_by_libraries import extract_by_libraries_ast
from data_analyze.analyze_engine import analyze_all_files
from database.dal_mongo import get_db_connector
from database.data.libraries_data import data

app = FastAPI()

PYTHON = "python"
DAL = get_db_connector(data)

@app.post("/files", status_code=status.HTTP_201_CREATED)
async def get_files(request: Request):
    try:
        result: dict = await request.json()
        error_handler.post_request(client_data=result)
        org = create_vcs_connector(token=result["token"], organization=result["organization"],
                                   vcs_type=result["vcs_type"])
        files = extract_by_libraries_ast(org.get_files_from_organization(), DAL.get_libraries_names(PYTHON))
        return analyze_all_files(files, PYTHON, DAL)
    except ValueError as error:
        return JSONResponse({"Error": str(error)}, status_code=status.HTTP_400_BAD_REQUEST)
    except TypeError as error:
        return JSONResponse({"Error": str(error)}, status_code=status.HTTP_400_BAD_REQUEST)


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
    uvicorn.run("server:app", host="localhost", port=80, reload=True)
