from typing import Optional

from pydantic import BaseModel


class Operation(BaseModel):
    uri: str
    term: Optional[str]

