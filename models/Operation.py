from typing import Optional

from pydantic import BaseModel


class Operation(BaseModel):
    uri: Optional[str]
    term: Optional[str]

