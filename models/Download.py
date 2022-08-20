from typing import Optional

from pydantic import BaseModel


class Download(BaseModel):
    url: str
    type: str
    note: Optional[str]
    version: Optional[str]