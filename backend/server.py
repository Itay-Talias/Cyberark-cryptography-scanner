from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import List

app = FastAPI()
#, status_code = status.HTTP_200_OK
@app.get("/files")
def get_files() -> List[dict]:
    pass
    # try:
    #     transactions = db_manger.get_all_transactions()
    # except pymysql.MySQLError as error:
    #     raise HTTPException(
    #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)
    # return transactions


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