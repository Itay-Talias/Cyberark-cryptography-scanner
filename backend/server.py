import uuid
from threading import Thread
from fastapi import FastAPI, status, Request, Cookie
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.responses import JSONResponse
from error_handler import error_handler
from vcs_api.vcs_factory import create_vcs_connector
from extract_files.extract_by_libraries import extract_by_libraries_ast
from data_analyze.analyze_engine import analyze_all_files
from typing import Union
from database.dal_mongo import get_db_connector


app = FastAPI()

PYTHON = "python"
DAL = get_db_connector()


def scan(_id, result):
    org = create_vcs_connector(token=result["token"], organization=result["organization"],
                               vcs_type=result["vcs_type"])
    files = extract_by_libraries_ast(org.get_files_from_organization(), DAL.get_libraries_names(PYTHON))
    results = analyze_all_files(files, PYTHON, DAL)
    DAL.add_results(_id, results)


@app.post("/scan", status_code=status.HTTP_201_CREATED)
async def start_scan(request: Request):
    try:
        result: dict = await request.json()
        error_handler.post_request(client_data=result)
        _id = uuid.uuid1()
        tread = Thread(target=scan, args=(_id, result))
        tread.start()
        response = JSONResponse(content={"id": str(_id)})
        return response
    except ValueError as error:
        return JSONResponse({"Error": str(error)}, status_code=status.HTTP_400_BAD_REQUEST)
    except TypeError as error:
        return JSONResponse({"Error": str(error)}, status_code=status.HTTP_400_BAD_REQUEST)


@app.get("/results", status_code=status.HTTP_200_OK)
async def get_results(scan_id: Union[str, None] = Cookie(default=None)):
    try:
        return DAL.get_results(scan_id)
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
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
