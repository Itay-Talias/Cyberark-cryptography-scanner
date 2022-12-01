from pydantic import BaseModel

class File(BaseModel):
    repo: str
    path: str
    file: str