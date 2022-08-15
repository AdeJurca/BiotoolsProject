from typing import List

from pydantic import BaseModel


class Link(BaseModel):
    url: str
    type: List[str]
    note: str

